#!/usr/bin/python
"""A class Place that inherits from BaseModel."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Module of a place


    Attributes:
        city_id (str): it will be the City.id
        user_id (str): it will be the User.id
        name (str): Describes the name of a place
        description (str): Describes a place
        number_rooms (int): Shows the number of rooms
        number_bathrooms (int): Shows the number of bathrooms
        max_guest (int): Shows the maximum number of guests
        price_by_night (int): Shows the price per night
        latitude (float): Shows the latitude of a place
        longitude (float): Shows the longitude of a place
        amenity_ids (list): it will be the list of Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
