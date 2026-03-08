import bcrypt
import logging
from fastapi import APIRouter, HTTPException
from data.login import get_user_by_email, verify_password

route = APIRouter()

@route.post("/login")
def login(email: str, password: str):
    user = get_user_by_email(email)  # busca só pelo email
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password.")
    
    # compara a senha digitada com o hash armazenado
    if verify_password(password, user.password):
        return {"message": "Login successful.", "user": {"name": user.name, "email": user.email, "password": user.password}}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password.")
