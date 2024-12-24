
from pymongo.mongo_client import MongoClient


MONGO_URI = "mongodb+srv://erpBackend:nxBpsyvI0oJrXxyy@cluster0.uo3rphs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

db = client.practice_fastapi
rawItem_collection = db.RawItems
# meal_collection = db.meals
# feedback_collection = db.feedback_collection
# user_collection = db.user_collection
