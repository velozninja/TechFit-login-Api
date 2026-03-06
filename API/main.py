"""this is the main file for the API, it contains the endpoints for the user management and home page"""
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, HTTPException
from data.login import register_user, get_user_by_email, remove_user
from data.database import Session, Usuario
from data.valid import Userschema
import logging


login_api = FastAPI()
@login_api.get("/home")
def home():
    return {"message": "Welcome to the home page."}
"""this function endpoint register a new user"""
@login_api.post("/register")
def register(user: Userschema):
    get_user = get_user_by_email(user.email)
    if get_user:
        logging.warning(f"Attempt to register with existing email: {user.email}")
        raise HTTPException(status_code=400, detail="User already exists.")
    success = register_user(user.name, user.email, user.password)
    if not success:
        raise HTTPException(status_code=400, detail="User already exists.")
    return {"message": "User registered successfully."}
"""this function endpoint get the user by email"""
@login_api.get("/user")
def get_user(email: str):
    user = get_user_by_email(email)
    if user:
        return {"message": "get user successfully.", "user": user}
    else:
        return {"message": "User not found."}
"""this function endpoint delete the user by email"""
@login_api.delete("/user")
def delete_user(email: str):
    remove_user(email)
    return {"message": "User deleted successfully."}
"""this function endpoint get all users in the database"""
@login_api.get("/users")
def get_all_users():
    session = Session()
    users = session.query(Usuario).all()
    session.close()
    if users == None:
        return {"message": "No users found."}
    else:
      return {"message": "get all users successfully.", "users": users}

"""this function run the API in the host"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(login_api, host="0.0.0.0", port=8000)