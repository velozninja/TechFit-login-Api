
"""configrations for databse sensive information"""
#imports
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
import logging

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")

# Database URL construction for PostgreSQL
if DB_TYPE == "postgresql":
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", )
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_NAME = os.getenv("DB_NAME", "techfit_db")
    DATABASE_URL = os.getenv("DATABASE_URL")
    logging.info("Using PostgreSQL database.")
else:
    DATABASE_URL = None
    logging.error("não autorizado")

    