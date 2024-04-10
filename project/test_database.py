import pytest
from testcontainers.mongodb import MongoDbContainer
import os
import main

# https://testcontainers.com/guides/getting-started-with-testcontainers-for-python

db = MongoDbContainer("mongo:7.0.7").with_exposed_ports(27017)
test_database_name = "test_tbd"

@pytest.fixture(scope="module", autouse=True)
def setup(request):
    # setup code
    db.start()

    def cleanup():
        # teardown code
        db.stop()

    request.addfinalizer(cleanup)
    
    # Mongo setup for tests 
    # os.environ["MONGO_HOST"] = db.get_container_host_ip()
    # os.environ["MONGO_PORT"] = db.get_exposed_port(27018)
    os.environ["MONGO_DB"] = test_database_name


@pytest.fixture(scope="function", autouse=True)
def setup_data():
    """Ensure each test starts with an empty database"""
    db.get_connection_client().drop_database(test_database_name)


def test_do_stuff(): 
    response = main.do_stuff("Testing from test module")
    print(response)
    # assert False