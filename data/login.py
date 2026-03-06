"""User authentication and management package.

This module provides functions for user registration, retrieval, and deletion.
"""
try:
    from . import database as db
    from . import valid as vd
except ImportError:
    import database as db
    import valid as vd

import bcrypt
import logging
from sqlalchemy.orm import sessionmaker

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
session = db.Session()

def register_user(name: str, email: str, password: str):
    try:
        user_data = vd.Userschema(name=name, email=email, password=password)
        psw = user_data.password.encode()
        hashed_password = bcrypt.hashpw(psw, bcrypt.gensalt())
        
        result = db.add_user(name=user_data.name, email=user_data.email, password=hashed_password)
        if result is None:
            logging.warning(f"User with email {email} already exists.")
            return False
        logging.info(f"User {user_data.name} registered successfully.")
        return True
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        return False  
def remove_user(email: str):
    try:
        db.remove_user(email)
        logging.info(f"User with email {email} removed successfully.")
    except Exception as e:
        logging.error(f"Error removing user: {e}")
def get_user_by_email(email: str):
    try:
        user = db.get_user_by_email(email)
        if user:
            logging.info(f"User with email {email} retrieved successfully.")
            return user
        else:
            logging.warning(f"No user found with email {email}.")
            return None
    except Exception as e:
        logging.error(f"Error retrieving user: {e}")
        return None
                                                                                                      