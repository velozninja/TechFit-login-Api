from pydantic import BaseModel, EmailStr, field_validator
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

aproved = False

class Userschema(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        global aproved
        if len(value) < 8:
            logging.error('Password validation failed: Password must be at least 8 characters long')
            aproved = False
            raise ValueError('Password must be at least 8 characters long')
        
        logging.info('Password validation passed')
        aproved = True
        return value