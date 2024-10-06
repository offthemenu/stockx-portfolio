import os
import pymongo
from pymongo import MongoClient, errors
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId

# Load environment variables from .env file
load_dotenv()
connectionString = os.getenv("connectionString")

# Create a MongoDB client
client = MongoClient(connectionString)

# Access the database
db = client["stockxData"]

# Create a time-series collection for price history. Comment out once completed for the first time.

# try:
#     db.create_collection(
#         "priceHistory",
#         timeseries={
#             "timeField": "date",
#             "metaField": "productId",
#             "granularity": "hours"
#         }
#     )
#     print("Time-series collection for price history created!")
# except errors.PyMongoError as e:
#     print(f"An error occurred while creating the collection: {e}")

priceHistoryCollection = db["priceHistory"]

# Add record
try:

    priceHistoryData = [
        {"productId": "123abc", "date": datetime(2022, 1, 1, 0, 0), "price": 250, "volume": 23},
        {"productId": "123abc", "date": datetime(2022, 1, 2, 0, 0), "price": 246, "volume": 94},
        {"productId": "123abc", "date": datetime(2022, 1, 3, 0, 0), "price": 287, "volume": 78},
        {"productId": "456def", "date": datetime(2022, 1, 1, 0, 0), "price": 254, "volume": 33},
        {"productId": "456def", "date": datetime(2022, 1, 2, 0, 0), "price": 259, "volume": 50},
        {"productId": "456def", "date": datetime(2022, 1, 3, 0, 0), "price": 260, "volume": 47},
        {"productId": "789ghi", "date": datetime(2022, 1, 1, 0, 0), "price": 288, "volume": 32},
        {"productId": "789ghi", "date": datetime(2022, 1, 2, 0, 0), "price": 276, "volume": 87},
        {"productId": "789ghi", "date": datetime(2022, 1, 3, 0, 0), "price": 215, "volume": 46},
        ]

    priceHistoryCollection.insert_many(priceHistoryData)

    print(f"price history data added successfully!")

except pymongo.errors.PyMongoError as e:
    print(f"An error occurred while adding price history: {e}")
