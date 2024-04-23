from pymongo import MongoClient


def mongo():
    """Establish a MongoDB Connection."""

    # Return the Mongo connection
    client = MongoClient(host="localhost", port=27017)
    print(f"Connected To Mongo Client @ {client.HOST}:{client.PORT}")
    return client


import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase

DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["database_name"]


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
