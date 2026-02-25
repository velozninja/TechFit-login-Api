from fastapi import FastAPI, HTTPException
from data.login import register_user
from data.login import get_user_by_email
from data.login import remove_user
from data.database import Session, Usuario
from data.valid import Userschema
import logging

login_api = FastAPI()
@login_api.get("/home")
def home():
    return {"message": "Welcome to the home page."}

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

@login_api.get("/user")
def get_user(email: str):
    user = get_user_by_email(email)
    if user:
        return {"message": "get user successfully.", "user": user}
    else:
        return {"message": "User not found."}

@login_api.delete("/user")
def delete_user(email: str):
    remove_user(email)
    return {"message": "User deleted successfully."}
@login_api.get("/users")
def get_all_users():
    session = Session()
    users = session.query(Usuario).all()
    session.close()
    return {"message": "get all users successfully.", "users": users}

# Vercel compatibility
app = login_api