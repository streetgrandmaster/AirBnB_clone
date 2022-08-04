#!/usr/bin/python
"""A class Review that inherits from BaseModel."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Module of a review


    Attributes:
        place_id (str): it will be the Place.id
        user_id (str): it will be the User.id
        text (str): Shows a review
    """
    place_id = ""
    user_id = ""
    text = ""
