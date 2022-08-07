#!/usr/bin/python3
"""Unittest cases for FileStorage class"""
import unittest
import inspect
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine import file_storage
from models.engine.file_storage import FileStorage


class TestFileStorageDocs(unittest.TestCase):
    """Tests for FileStorage documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from FileStorage members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.flsfuncs = inspect.getmembers(FileStorage, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.flsfuncs = []

    def test_file_storage_conforms_pep8(self):
        """Test models/engine/file_storage.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testfile_storage_conforms_pep8(self):
        """Test that tests/test_models/test_engine/test_file_storage.py
         conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_engine/\
test_file_storage.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for FileStorage class docstring"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for file_storage functions docstrings"""
        for func in self.flsfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Fls = FileStorage()
obj = BaseModel()


class TestFileStorage(unittest.TestCase):
    """Tests for HBNBCommand class"""
    @classmethod
    def setUp(self):
        """Makes sure all prerequisites for our tests are available"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        """Cleans all those prerequisites"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Tests 'all' returns the dictionary __objects"""
        my_dict = Fls.all()
        self.assertIsNotNone(my_dict)
        self.assertEqual(type(my_dict), dict)
        self.assertIs(my_dict, Fls._FileStorage__objects)

    def test_all_args(self):
        """Tests when 'all' has an argument"""
        with self.assertRaises(TypeError):
            Fls.all(None)

    def test_new(self):
        """Tests 'new' sets in __objects the obj with
        key <obj class name>.id"""
        Fls.new(obj)
        my_dict = Fls.all()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(type(my_dict), dict)
        self.assertEqual(my_dict[key] is obj, True)

    def test_new_extrargs(self):
        """Tests when 'new' has an extra argument"""
        with self.assertRaises(TypeError):
            Fls.new(obj, 0)

    def test_save(self):
        """Tests 'save' serializes __objects to the JSON file
        (path: __file_path)"""
        Fls.new(obj)
        Fls.save()
        contents = ""
        with open("file.json", "r") as f:
            contents = f.read()
            self.assertEqual(Fls.all()["BaseModel." + obj.id], obj)
            self.assertIn("BaseModel." + obj.id, contents)

    def test_save_args(self):
        """Tests when 'save' has an argument"""
        with self.assertRaises(TypeError):
            Fls.save(None)

    def test_reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
         (__file_path) exists ; otherwise, do nothing. If the file doesn't
         exist, no exception should be raised)"""
        Fls.new(obj)
        Fls.save()
        Fls.reload()
        self.assertIn("BaseModel." + obj.id, Fls._FileStorage__objects)

    def test_reload_args(self):
        """Test when 'reload' has an argument"""
        with self.assertRaises(TypeError):
            Fls.reload(None)


if __name__ == "__main__":
    unittest.main()
