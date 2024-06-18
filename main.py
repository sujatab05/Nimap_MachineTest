from fastapi import FastAPI, HTTPException
from typing import List, Dict
import os
import json
from pydantic import BaseModel

app = FastAPI()

# Define the User model using Pydantic
class User(BaseModel):
    name: str
    email: str
    age: int

# Path to the data directory and JSON file
DATA_DIR = "./data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

# Ensure the data directory and users file exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f:
        json.dump([], f)

@app.get("/")
def read_root():
    return {"message": "Hello, World"}

@app.get("/users")
def get_users():
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    return users

@app.post("/users", response_model=Dict[str, str])
def add_user(user: User):
    """
    Adds a new user to the users.json file.

    Args:
        user (User): The user data to add.

    Returns:
        dict: A success message with user data.
    """
    # Load existing users from the file
    with open(USERS_FILE, 'r') as f:
        users = json.load(f)
    
    # Convert user Pydantic model to dictionary and add to users list
    users.append(user.dict())

    # Save the updated users list back to the file
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

    return {"message": "User added successfully"}
