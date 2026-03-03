# -*- coding: utf-8 -*-
from sqlalchemy import String, create_engine, Integer, Column
from sqlalchemy.orm import sessionmaker, declarative_base
import logging
try:
    from .config import DATABASE_URL
except ImportError:
    from config import DATABASE_URL

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "user_login"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

database = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=database)


def add_user(nome, email, senha):
    session = Session()
    existing_user = session.query(Usuario).filter_by(email=email).first()
    if existing_user:
        logging.info(f"User {nome} already exists.")
        session.close()
        return None
    new_user = Usuario(nome=nome, email=email, senha=senha)
    session.add(new_user)
    session.commit()
    session.close()
    return new_user

def remove_user(email):
    session = Session()
    user_to_remove = session.query(Usuario).filter_by(email=email).first()
    if user_to_remove:
        logging.info(f"User {user_to_remove.nome} found for removal.")
        session.delete(user_to_remove)
        session.commit()
        logging.info("User removed successfully.")
    session.close()
def get_user_by_email(email):
    session = Session()
    user = session.query(Usuario).filter_by(email=email).first()
    if user:
        logging.info("User retrieved successfully.")
    session.close()
    return user