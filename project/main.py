
import database
import logging


def do_stuff(desc="default placeholder text") -> dict: 
    """Placeholder for interacting with MongoDB"""

    db = database.mongo_db()
    collection = db.name_this_collection
    print(f"Connected to Mongo {db.name}:{collection.name}")

    # Insert test data 
    data1 = {
        "user": "me", 
        "description": desc
    }
    data1_id = collection.insert_one(data1).inserted_id
    print(f"Inserted ID: {data1_id}")

    # Read data from db 
    data1_response = collection.find_one(data1_id)
    print(f"found{data1_response}")

    return data1_response


if __name__ == "__main__": 
    do_stuff(f"Executing from mongodb.py main")
    