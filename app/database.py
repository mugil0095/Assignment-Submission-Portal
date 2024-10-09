from motor.motor_asyncio import AsyncIOMotorClient

# Connect to MongoDB using AsyncIOMotorClient
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["assignment_portal"]

# Connect to MongoDB using AsyncIOMotorClient
users_collection = db["users"]
admins_collection = db["admins"]
assignments_collection = db["assignments"]
