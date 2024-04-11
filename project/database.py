from pymongo import MongoClient


def mongo(): 
    """Establish a MongoDB Connection."""

    # Return the Mongo connection
    client = MongoClient(host="localhost", port=27017)
    print(f"Connected To Mongo Client @ {client.HOST}:{client.PORT}")
    return client
