import logging
from project import database


def do_stuff(desc="default placeholder text") -> dict: 
    """Placeholder for interacting with MongoDB"""

    client = database.mongo()
    db = client["tbd"]
    collection = db.name_this_collection
    logging.info(f"Connected to Mongo {db.name}:{collection.name}")

    # Insert test data 
    data1 = {
        "user": "me", 
        "description": desc
    }
    data1_id = collection.insert_one(data1).inserted_id
    logging.info(f"Inserted ID: {data1_id}")

    # Read data from db 
    data1_response = collection.find_one(data1_id)
    logging.info(f"found{data1_response}")

    return data1_response


if __name__ == "__main__": 
    do_stuff(f"Executing from mongodb.py main")
    