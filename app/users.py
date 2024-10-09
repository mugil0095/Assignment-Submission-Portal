from fastapi import APIRouter, HTTPException, Depends
from app.auth import get_password_hash, verify_password, create_access_token
from app.database import users_collection, assignments_collection, admins_collection
from app.models import UserCreate, UserLogin, Assignment
from bson.objectid import ObjectId
from datetime import datetime

# Create a router for user endpoints
router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate):
    # Check if the username is already taken
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Hash the password and create a new user record
    hashed_password = get_password_hash(user.password)
    new_user = {"username": user.username, "password": hashed_password}
    await users_collection.insert_one(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
async def login_user(user: UserLogin):
    # Validate user credentials and create an access token if valid
    db_user = await users_collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/upload")
async def upload_assignment(assignment: Assignment):
    # Save the uploaded assignment to the database with a timestamp
    assignment_data = assignment.dict()
    assignment_data["timestamp"] = datetime.utcnow().isoformat()
    await assignments_collection.insert_one(assignment_data)
    return {"message": "Assignment uploaded successfully"}

@router.get("/admins")
async def get_all_admins():
    # Retrieve a list of all admins
    admins = await admins_collection.find({}).to_list(100)
    return [{"username": admin["username"]} for admin in admins]
