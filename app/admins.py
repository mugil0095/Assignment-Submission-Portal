from fastapi import APIRouter, HTTPException, Depends
from app.database import admins_collection, assignments_collection
from app.models import UserCreate
from app.auth import get_password_hash  # Ensure this is correctly imported
from bson.objectid import ObjectId

router = APIRouter()    # Create a router for the admin endpoints

@router.post("/register")
async def register_admin(admin: UserCreate):
    # Create a router for the admin endpoints
    existing_admin = await admins_collection.find_one({"username": admin.username})
    if existing_admin:
        raise HTTPException(status_code=400, detail="Admin already registered")
    
    # Hash the password and create a new admin record
    hashed_password = get_password_hash(admin.password)
    new_admin = {"username": admin.username, "password": hashed_password}
    await admins_collection.insert_one(new_admin)
    return {"message": "Admin registered successfully"}

@router.get("/assignments")
async def view_assignments(admin_username: str):
    # Retrieve assignments tagged to the specified admin
    assignments = await assignments_collection.find({"admin": admin_username}).to_list(100)
    return [{"id": str(assignment["_id"]), "userId": assignment["userId"], "task": assignment["task"], "timestamp": assignment["timestamp"]} for assignment in assignments]

@router.post("/admins/assignments/{user_id}/{task}/accept")
async def accept_assignment(user_id: str,task: str):
    # Update the status of the assignment to 'accepted'
    result = await assignments_collection.update_many(
        {"userId": user_id, "task": task,"status": {"$ne": "accepted"}}, 
        {"$set": {"status": "accepted"}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"message": "Assignment accepted"}

@router.post("/admins/assignments/{user_id}/{task}/reject")
async def reject_assignment(user_id: str, task: str):
    # Update the status of the assignment to 'rejected'
    result = await assignments_collection.update_many(
        {"userId": user_id, "task": task,"status": {"$ne": "rejected"}}, 
        {"$set": {"status": "rejected"}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return {"message": "Assignment rejected"}
