from pymongo import MongoClient

# Connect to the MongoDB server running locally
client = MongoClient("mongodb://localhost:27017/")

db = client.stockx_project

collection = db.products