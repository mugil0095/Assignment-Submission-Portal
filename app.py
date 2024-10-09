import streamlit as st
import requests

# Constants
API_URL = "http://localhost:8000"  # Update to your FastAPI URL if different

# User Functions
def user_register():
    st.subheader("User Registration")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Register"):
        response = requests.post(f"{API_URL}/users/register", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("User registered successfully!")
        else:
            st.error(response.json().get("detail", "Error during registration"))

def user_login():
    st.subheader("User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        response = requests.post(f"{API_URL}/users/login", json={"username": username, "password": password})
        if response.status_code == 200:
            token = response.json().get("access_token")
            st.session_state['token'] = token
            st.success("Login successful!")
        else:
            st.error(response.json().get("detail", "Error during login"))

def upload_assignment():
    if 'token' not in st.session_state:
        st.error("You need to log in to upload assignments.")
        return

    st.subheader("Upload Assignment")
    user_id = st.text_input("User ID")
    task = st.text_input("Task Description")

    if st.button("Upload"):
        headers = {"Authorization": f"Bearer {st.session_state['token']}"}
        response = requests.post(f"{API_URL}/users/upload", json={"userId": user_id, "task": task}, headers=headers)
        if response.status_code == 200:
            st.success("Assignment uploaded successfully!")
        else:
            st.error(response.json().get("detail", "Error uploading assignment"))

def view_all_admins():
    st.subheader("View All Admins")
    response = requests.get(f"{API_URL}/users/admins")
    if response.status_code == 200:
        admins = response.json()
        for admin in admins:
            st.write(admin['username'])
    else:
        st.error("Failed to retrieve admins.")

# Admin Functions
def admin_register():
    st.subheader("Admin Registration")
    username = st.text_input("Username", key="admin_username")
    password = st.text_input("Password", type='password', key="admin_password")

    if st.button("Register Admin"):
        response = requests.post(f"{API_URL}/admins/register", json={"username": username, "password": password})
        if response.status_code == 200:
            st.success("Admin registered successfully!")
        else:
            st.error(response.json().get("detail", "Error during registration"))

def view_assignments():
    admin_username = st.text_input("Admin Username", key="view_admin_username")

    if st.button("View Assignments"):
        response = requests.get(f"{API_URL}/admins/assignments?admin_username={admin_username}")
        if response.status_code == 200:
            assignments = response.json()
            for assignment in assignments:
                st.write(f"User ID: {assignment['userId']}, Task: {assignment['task']}, Timestamp: {assignment['timestamp']}")
        else:
            st.error("Failed to retrieve assignments.")

def accept_assignment():
    user_id = st.text_input("User ID to accept", key="accept_user_id")
    task = st.text_input("Task to accept", key="accept_task")

    if st.button("Accept Assignment"):
        response = requests.post(f"{API_URL}/admins/assignments/{user_id}/{task}/accept")
        if response.status_code == 200:
            st.success("Assignment accepted!")
        else:
            st.error("Error accepting assignment")

def reject_assignment():
    user_id = st.text_input("User ID to reject", key="reject_user_id")
    task = st.text_input("Task to reject", key="reject_task")

    if st.button("Reject Assignment"):
        response = requests.post(f"{API_URL}/admins/assignments/{user_id}/{task}/reject")
        if response.status_code == 200:
            st.success("Assignment rejected!")
        else:
            st.error("Error rejecting assignment")

# Streamlit UI
st.title("Assignment Submission Portal")

menu = st.sidebar.selectbox("Choose Role", ["User", "Admin"])

if menu == "User":
    user_option = st.sidebar.selectbox("Select Action", ["Register", "Login", "Upload Assignment", "View Admins"])
    if user_option == "Register":
        user_register()
    elif user_option == "Login":
        user_login()
    elif user_option == "Upload Assignment":
        upload_assignment()
    elif user_option == "View Admins":
        view_all_admins()

elif menu == "Admin":
    admin_option = st.sidebar.selectbox("Select Action", ["Register", "View Assignments", "Accept Assignment", "Reject Assignment"])
    if admin_option == "Register":
        admin_register()
    elif admin_option == "View Assignments":
        view_assignments()
    elif admin_option == "Accept Assignment":
        accept_assignment()
    elif admin_option == "Reject Assignment":
        reject_assignment()
