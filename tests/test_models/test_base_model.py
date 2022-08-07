#!/usr/bin/python3
"""Unittest cases for BaseModel class"""
import inspect
import pep8
import unittest
from unittest import mock
from models import base_model
from models.base_model import BaseModel


class TestBaseModelDocs(unittest.TestCase):
    """Tests for BaseModel documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from BaseModel members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.basefuncs = inspect.getmembers(BaseModel, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.basefuncs = []

    def test_base_model_conforms_pep8(self):
        """Test models/base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testbase_model_conforms_pep8(self):
        """Test that tests/test_models/test_base_model.py
         conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_base_\
model.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for BaseModel class docstring"""
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for base_model functions docstrings"""
        for func in self.basefuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


obj = BaseModel()
obj.name = "My First Model"
obj.my_number = 89


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertIs(type(obj), BaseModel)
        self.assertTrue(hasattr(obj, "name"))
        self.assertIn("name", obj.__dict__)
        self.assertTrue(type(obj.__dict__["name"]), 'str')
        self.assertTrue(hasattr(obj, "my_number"))
        self.assertIn("my_number", obj.__dict__)
        self.assertTrue(type(obj.__dict__["my_number"]), 'int')
        self.assertTrue(hasattr(obj, "id"))
        self.assertIn("id", obj.__dict__)
        self.assertTrue(type(obj.__dict__["id"]), 'str')
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertIn("created_at", obj.__dict__)
        self.assertTrue(type(obj.__dict__["created_at"]), 'datetime')
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertIn("updated_at", obj.__dict__)
        self.assertTrue(type(obj.__dict__["updated_at"]), 'datetime')

    @mock.patch('models.storage')
    def test_id(self, mock_st):
        """Tests uniqueness of different instances' id"""
        other_obj = BaseModel()
        self.assertTrue(mock_st.new.called)
        self.assertNotEqual(obj.id, other_obj.id)

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(obj.to_dict()["name"]), str)
        self.assertIs(type(obj.to_dict()["my_number"]), int)
        self.assertIs(type(obj.to_dict()["__class__"]), str)
        self.assertIs(type(obj.to_dict()["id"]), str)
        self.assertIs(type(obj.to_dict()["created_at"]), str)
        self.assertIs(type(obj.to_dict()["updated_at"]), str)

    def test_to_dict_arg(self):
        """Tests when 'to_dict' has an argument"""
        with self.assertRaises(TypeError):
            obj.to_dict(None)

    def test_str(self):
        """Tests'str' returns the informal representation of BaseModel
         objects"""
        string = "[BaseModel] ({}) {}".format(obj.id, obj.__dict__)
        self.assertEqual(string, str(obj))

    @mock.patch('models.storage')
    def test_save(self, mock_st):
        """Tests 'save' updates the public instance attribute 'updated_at'
         with the current datetime"""
        time_c1 = obj.created_at
        time_u1 = obj.updated_at
        obj.save()
        time_c2 = obj.created_at
        time_u2 = obj.updated_at
        self.assertNotEqual(time_u1, time_u2)
        self.assertEqual(time_c1, time_c2)
        self.assertTrue(mock_st.save.called)

    def test_save_with_arg(self):
        """Tests when 'save' has an argument"""
        with self.assertRaises(TypeError):
            obj.save(None)
