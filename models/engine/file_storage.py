#!/usr/bin/python3
"""A class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"City": City, "Amenity": Amenity, "BaseModel": BaseModel,
           "State": State, "Place": Place, "Review": Review, "User": User}


class FileStorage:
    """Module of file storage


    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by
                                <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        my_obj = {}
        for key in self.__objects:
            my_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON
        file (__file_path) exists ; otherwise, do nothing. If the file
        doesn't exist, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                ob = json.load(f)
            for key in ob:
                self.__objects[key] = classes[ob[key]["__class__"]](**ob[key])
        except FileNotFoundError:
            pass
