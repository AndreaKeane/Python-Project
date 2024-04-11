from pymongo import MongoClient
import os


def mongo_client(): 
    """Establish a MongoDB Connection."""

    # Using environment variables so our test fixtures can connect to a test instance
    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", 27017)

    # Return the Mongo connection
    client = MongoClient(host=host, port=port)
    print(f"Connected To Mongo Client @ {client.HOST}:{client.PORT}")
    return client


def mongo_db(db_name=None): 
    """Connect to a MongoDB Database using Env Variables"""
    # Keeping the env variable lookups in one place.

    # First, check for a DB name stored in os.getenv("MONGO_DB_NAME") - used by pytest
    # Then, if the env variable is empty, use the DB name that's passed in
    list = [os.getenv("MONGO_DB_NAME"), db_name]
    db_name = next(name for name in list if name)

    # Connect to the database name identified
    return mongo_client()[db_name]