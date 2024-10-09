from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"     # Replace with a strong secret key
ALGORITHM = "HS256"                # Algorithm for encoding JWT tokens
ACCESS_TOKEN_EXPIRE_MINUTES = 30   # Token expiration time

# Create a password context for hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    # Verify if the provided password matches the hashed password
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    # Hash the password for secure storage
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    # Create a JWT token with an expiration time
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    # Decode the JWT token and return the subject
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
