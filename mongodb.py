from pymongo import MongoClient


if __name__ == "__main__": 

    # Establish a connection
    client = MongoClient('localhost', port=27017)

    # Create or Switch Database
    db = client.testing_db

    # Create or Switch Collection 
    collection = db.testing_collection

    # Insert test data 
    data1 = {
        "user": "me", 
        "description": "testing local docker setup"
    }
    data1_id = collection.insert_one(data1).inserted_id
    print(f"Inserted ID: {data1_id}")

    # Read data from db 
    data1_response = collection.find_one(data1_id)
    print(data1_response)
