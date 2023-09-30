from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#rom main import col


import os
from dotenv import load_dotenv

load_dotenv()


class MongoConnection:
    def __init__(self):
        #SE EXTRAEN LOS DATOS DE CREDENCIALES DEL .ENV
        user = os.getenv("MONGO_USER")
        password = os.getenv("MONGO_PASSWORD")
        db_hostname = os.getenv("MONGO_HOST")
        uri = f"mongodb+srv://{user}:{password}@{db_hostname}/?retryWrites=true&w=majority"

        #client = MongoClient(uri)

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))

    def test_connection(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)



if __name__ == "__main__":
    MongoConnection().test_connection()