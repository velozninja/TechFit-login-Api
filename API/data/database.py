from sqlalchemy import String, create_engine, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column
import logging

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    senha = Column(String(255), nullable=False, unique=True)

database = create_engine("sqlite:///database.db", echo=True)
Base.metadata.create_all(database)
Session = sessionmaker(bind=database)


def add_user(nome, email, senha):
    new_user = Usuario(nome=nome, email=email, senha=senha)
    user = Usuario(nome=nome, email=email, senha=senha)
    if user == new_user:
        logging.info(f"User {nome} already exists.")
        return
    session = Session()
    session.add(new_user)
    session.commit()
    session.close()
    return new_user

def remove_user(email):

    session = Session()
    user_to_remove = session.query(Usuario).filter_by(email=email).first()
    if user_to_remove:
        logging.info(f"User {user_to_remove.nome} found for removal.")
        return
    if user_to_remove:
  
        session.delete(user_to_remove)
        logging.info("User removed successfully.")
        session.commit()
    session.close()
def get_user_by_email(email):
    session = Session()
    user = session.query(Usuario).filter_by(email=email).first()
    logging.info("User retrieved successfully.")
    session.close()
    return user