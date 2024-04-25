import logging
import pytest
from fastapi.testclient import TestClient
from src.app.app import app

from testcontainers.mongodb import MongoDbContainer

# https://testcontainers.com/guides/getting-started-with-testcontainers-for-python
mongo = MongoDbContainer("mongo:7.0.7")

client = TestClient(app)

# TODO: There's a lot of copy-paste between here and test_database. Can we simplify?


@pytest.fixture(scope="module", autouse=True)
def setup_testcontainer(request):
    mongo.start()

    def remove_container():
        mongo.stop()

    request.addfinalizer(remove_container)


@pytest.fixture(scope="function", autouse=True)
def setup_data(monkeypatch):
    # Monkeypatching the real MongoDB connection with a test container
    def test_mongo():
        logging.info("Replacing MongoDB Client with Test Container")
        return mongo.get_connection_client()

    monkeypatch.setattr("src.database.mongo", test_mongo)

    # Yielding to the test logic
    yield

    # DB Cleanup = Drop any databases that were created by the application s.t. each test starts with an empty MongoDB
    client = mongo.get_connection_client()
    for db in client.list_database_names():
        if db not in ["admin", "config", "local"]:
            client.drop_database(db)


def test_hello_world():

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.skip(reason="test-containers not working with Beanie")
def test_register_user():
    """https://fastapi-users.github.io/fastapi-users/latest/usage/routes/#post-register"""

    test_account = {
        "email": "king.arthur@camelot.bt",
        "password": "test-pass-123"
    }

    response = client.post(
        "/auth/register",
        json=test_account
    )

    assert response.status_code == 201
    assert response.json() == {
        "email": "testing@testing.com",
        "is_active": True,
        "is_superuser": False
    }