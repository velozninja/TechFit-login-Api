from pydantic import BaseModel, EmailStr, field_validator
import re
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
        pontuação = 0
        global aproved
        if len(value) < 8:
            if re.search(r'[A-Z]', value):
                pontuação += 1
            if re.search(r'[a-z]', value):
                pontuação += 1
            if re.search(r'[0-9]', value):
                pontuação += 1
            if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
                pontuação += 1

            if pontuação < 3:
                aproved = False
                logging.warning('Password validation failed: insufficient character types')

                raise ValueError('Password must contain at least 3 of the following: uppercase letters, lowercase letters, numbers, special characters')


        
        logging.info('Password validation passed')
        aproved = True
        return value