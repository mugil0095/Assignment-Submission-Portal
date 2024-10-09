from pydantic import BaseModel

# Define a model for user registration
class UserCreate(BaseModel):
    username: str
    password: str

# Define a model for user login
class UserLogin(BaseModel):
    username: str
    password: str

# Define a model for assignment submission
class Assignment(BaseModel):
    userId: str
    task: str
    admin: str
    timestamp: str

# Define a response model for assignment retrieval
class AssignmentResponse(BaseModel):
    id: str
    userId: str
    task: str
    timestamp: str
