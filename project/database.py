from pymongo import MongoClient
import os


def mongo(): 
    """Establish a MongoDB Connection."""

    # Using environment variables so our test fixtures can 
    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", 27017)
    db_name = os.getenv("MONGO_DB", "tbd")  # TODO: Have a better database name

    # Return the Mongo connection
    client = MongoClient(host=host, port=port)
    return client[db_name]

