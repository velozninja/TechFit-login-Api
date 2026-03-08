"""database connection and user management"""
#imports
from sqlalchemy import String, create_engine, Integer, Column
from sqlalchemy.orm import sessionmaker, declarative_base
import logging
import uuid

try:
    from .config import DATABASE_URL
except ImportError:
    from config import DATABASE_URL
#define the database model
Base = declarative_base()
#usuario base model
class Usuario(Base):
    __tablename__ = "user_login"

    id = Column( primary_key=True,default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False, unique=True)
#create the database connection
database = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=database)

"""this function add in the databse table new user with name, email and password
but first check if the email already exist in the database, if exist return None, else add the user and return the user"""
def add_user(name, email, password):
    session = Session()
    new_user = Usuario(name=name, email=email, password=password)
    if session.query(Usuario).filter_by(email=email).first():
        logging.warning(f"Attempt to add user with existing email: {email}")
        session.close()
        return None
    session.add(new_user)
    session.commit()
    session.close()
    return new_user
"""this function remove the user from the database by email, if the user exist remove it, else do nothing"""
def remove_user(email):
    session = Session()
    user_to_remove = session.query(Usuario).filter_by(email=email).first()
    if user_to_remove:
        logging.info(f"User {user_to_remove.name} found for removal.")
        session.delete(user_to_remove)
        session.commit()
        logging.info("User removed successfully.")
    session.close()
"""this function get the user from the database by email, if the user exist return it, else return None"""
def get_user_by_email(email):
    session = Session()
    user = session.query(Usuario).filter_by(email=email, ).first()
    if user:
        logging.info("User retrieved successfully.")
    session.close()
    return user

def get_user_psw(password):
    session = Session()
    user = session.query(Usuario).filter_by(password=password).first()
    if user:
        logging.info("User retrieved successfully.")
    session.close()
    return user