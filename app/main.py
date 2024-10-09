from fastapi import FastAPI
from app.users import router as user_router
from app.admins import router as admin_router

# Create a FastAPI application instance
app = FastAPI()

# Include user and admin routers with specific prefixes
app.include_router(user_router, prefix="/users")
app.include_router(admin_router, prefix="/admins")

@app.get("/")
async def root():
    # Root endpoint returning a welcome message
    return {"message": "Assignment Submission Portal"}
