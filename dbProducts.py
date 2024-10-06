import pymongo
from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

load_dotenv()
connectionString = os.getenv("connectionString")

client = MongoClient(connectionString)

db = client["stockxData"]
productsCollection = db["products"]

productData = {
    "stockxId": "123abc",
    "name": "Air Jordan 1 Retro High OG Bred",
    "releaseYear": 1985,
    "retailPrice": 160
}

try:
    productsCollection.insert_one(productData)
    print("Product Inserted to Data!")
except pymongo.errors.PyMongoError as e:
    print(f"An error occurred while adding the product: {e}")