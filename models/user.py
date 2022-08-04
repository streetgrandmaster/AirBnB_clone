#!/usr/bin/python
"""A class User that inherits from BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """Module of a user


    Attributes:
        email (str): A user's email
        password (str): A user's password
        first_name (str): A user's first name
        last_name (str): A user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
