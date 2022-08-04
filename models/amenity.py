#!/usr/bin/python3
"""A class Amenity that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Module of an amenity


    Attributes:
        name (str): Describes the name of an amenity
    """
    name = ""
