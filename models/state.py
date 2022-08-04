#!/usr/bin/python3
"""A class State that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """Module of a state


    Attributes:
        name (str): Describes the name of a state
    """
    name = ""
