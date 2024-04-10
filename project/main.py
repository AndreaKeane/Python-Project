
import database
import logging

def do_stuff(desc="default placeholder text") -> dict: 
    """Placeholder for interacting with MongoDB"""

    db = database.mongo()
    print(db)
    print(type(db).__name__)

    # Create or Switch Collection 
    collection = db.name_this_collection

    # Insert test data 
    data1 = {
        "user": "me", 
        "description": desc
    }
    data1_id = collection.insert_one(data1).inserted_id
    logging.debug(f"Inserted ID: {data1_id}")

    # Read data from db 
    data1_response = collection.find_one(data1_id)
    logging.debug(data1_response)

    return data1_response


if __name__ == "__main__": 
    do_stuff(f"Executing from mongodb.py main")
    