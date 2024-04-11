import logging

import pytest
from testcontainers.mongodb import MongoDbContainer

from project import main

# https://testcontainers.com/guides/getting-started-with-testcontainers-for-python
mongo = MongoDbContainer("mongo:7.0.7")


@pytest.fixture(scope="module", autouse=True)
def setup(request):
    mongo.start()

    def remove_container():
        mongo.stop()

    request.addfinalizer(remove_container)


@pytest.fixture(scope="function", autouse=True)
def setup_data():
    # Drop any databases that were created by the application s.t. each test starts with an empty MongoDB
    client = mongo.get_connection_client()
    for db in client.list_database_names():
        if db not in ["admin", "config", "local"]: 
            client.drop_database(db) 
    

def test_do_stuff(monkeypatch): 

    # Monkeypatching the real MongoDB connection with a test container
    def test_mongo(): 
        logging.info("Replacing MongoDB Client with Test Container")
        return mongo.get_connection_client()
    
    monkeypatch.setattr("project.database.mongo", test_mongo)

    # Proceed to run test with the patched MongoDB client
    response = main.do_stuff("Testing from test module")
    assert response