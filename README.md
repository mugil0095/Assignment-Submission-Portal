
# Assignment Submission Portal - Backend System 

## Overview
This backend system is designed for an assignment submission portal that supports two types of users: Users and Admins. Users can upload assignments, while Admins can view, accept, or reject these assignments.

## Prerequisites
Before setting up the application, ensure you have the following installed:

- Python (version 3.7 or higher)
- pip (Python package manager)
- MongoDB (version 4.x or higher) running locally or on a server

## Installation
### 1. Clone the Repository:
```
git clone <repository-url> 
cd assignment_submission_portal
```
### 2. Create a Virtual Environment:
```
python -m venv venv
source venv/bin/activate  #On Windows use `venv\Scripts\activate`
```
### 3. Install Dependencies:
```
pip install fastapi[all] motor passlib python-jose
```

## Configuration
### 1. MongoDB Connection:
Ensure MongoDB is running. The application connects to MongoDB at the default URL ```mongodb://localhost:27017```. You can modify the connection string in ```app/database.py``` if needed.
### 2. Secret Key:
Update the ```SECRET_KEY``` in ```app/auth.py``` to a secure value for JWT token encoding.

## Running the Application
### 1. Start the FastAPI Server:
Use the following command to run the application:
```
uvicorn app.main:app --reload
```
The ```--reload``` option allows for automatic reloading of the server on code changes.
### 2. Access the API:
The API will be available at ```http://127.0.0.1:8000```. You can access the interactive API documentation at ```http://127.0.0.1:8000/docs```.

## API Endpoints
### User Endpoints
- Register User:
   - Method: POST
   - Endpoint: ```/users/register```
   - Request Body:
     ```
     {
       "username": "string",
       "password": "string"
     }
     ```
- Login User:
   - Method: POST
   - Endpoint: ```/users/login```
   - Request Body:
     ```
     {
       "username": "string",
       "password": "string"
     }
     ```
- Upload Assignment:
   - Method: POST
   - Endpoint: ```/users/upload```
   - Request Body:
     ```
     {
       "userId": "string",
       "task": "string",
       "admin": "string"
     }
     ```
- Get All Admins
   - Method: GET
   - Endpoint: ```/users/admins```
   - Request Body:
     ```
     {
       "userId": "string",
       "task": "string",
       "admin": "string"
     }
     ```

## Admin Endpoints
- Register Admin:
   - Method: POST
   - Endpoint: ```/admins/register```
   - Request Body:
     ```
     {
       "username": "string",
       "password": "string",
     }
     ```
- Login Admin:
   - Method: POST
   - Endpoint: ```/admins/login```
   - Request Body:
     ```
     {
       "username": "string",
       "password": "string",
     }
     ```
- View Assignments:
   - Method: GET
   - Endpoint: ```/admins/assignments```
- Accept Assignment:
   - Method: POST
   - Endpoint: ```/admins/assignments/{user_id}/{task}/accept```
- Reject Assignment:
   - Method: POST
   - Endpoint: ```/admins/assignments/{user_id}/{task}/reject```

## Usage
After starting the server, you can use tools like Postman or cURL to interact with the API endpoints. The interactive API documentation at ```/docs``` allows you to test endpoints directly.
## Error Handling
- The application raises HTTP exceptions with appropriate status codes and messages for invalid operations, such as duplicate registrations, invalid login credentials, or attempts to accept/reject non-existent assignments.
## Conclusion
This documentation provides the necessary steps to set up and run the Assignment Submission Portal backend system. For further development or enhancements, ensure to maintain modularity and follow best practices for code management.


