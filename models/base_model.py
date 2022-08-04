#!/usr/bin/python3
"""A class BaseModel that defines a base of all other classes."""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Module of a base


    Attributes:
        if kwargs is not empty:
        each key of the dictionary is an attribute name
        each value of the dictionary is the value of this attribute name
    """
    def __init__(self, *args, **kwargs):
        """Initializes the base attributes


        Args:
            args(list): no-keyword argument, order is important
            kwargs(dict): key-worded argument, order is not important

        Returns:
            None
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key not in ['__class__']:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Represents the BaseModel objects as a string


        Returns:
            the 'informal' representing string
        """
        a, b, c = self.__class__.__name__, self.id, self.__dict__
        return("[{}] ({}) {}".format(a, b, c))

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return:
            a dictionary containing all keys/values of __dict__ of the instance
        """
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary['__class__'] = self.__class__.__name__
        return dictionary
