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
session = db.Session()  # Create a session at the module level to be used in functions

def register_user(name: str, email: str, password: str):
    try:
        db.Session()  # Test database session creation

        logging.info("Database session started successfully.")
        if session is None:
            logging.error("Failed to create database session.")
            return
        if not session.is_active:
            logging.error("Database session is not active.")
            return

        
        user_data = vd.Userschema(name=name, email=email, password=password)
        if user_data is None:
            logging.error("User data validation failed: No data returned.")
            return
        if vd.aproved is False:
            logging.error("User data validation failed: Password did not meet criteria.")
            return
        logging.info("User data validated successfully.")
        psw = user_data.password.encode()
        hashed_password = bcrypt.hashpw(psw, bcrypt.gensalt())
    

        
        
        db.add_user(nome=user_data.name, email=user_data.email, senha=hashed_password)
        logging.info(f"User {user_data.name} registered successfully.")
        
    except Exception as e:
        logging.error(f"Error registering user: {e}")  
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
                                                                                                      