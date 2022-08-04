#!/usr/bin/python3
"""A class City that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """Module of a city


    Attributes:
        state_id (str): it will be the State.id
        name (str): Describes the name of a city
    """
    state_id = ""
    name = ""
