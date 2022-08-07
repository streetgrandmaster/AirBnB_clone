#!/usr/bin/python3
"""Unittest cases for User class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import user
from models.user import User


class TestUserDocs(unittest.TestCase):
    """Tests for User documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from User members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.userfuncs = inspect.getmembers(User, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.userfuncs = []

    def test_user_conforms_pep8(self):
        """Test models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testuser_conforms_pep8(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(user.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for User class docstring"""
        self.assertTrue(len(User.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for user functions docstrings"""
        for func in self.userfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Usr = User()


class TestUser(unittest.TestCase):
    """Tests for User class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(Usr, "email"))
        self.assertIs(type(Usr.email), str)
        self.assertEqual(Usr.email, "")
        self.assertTrue(hasattr(Usr, "password"))
        self.assertIs(type(Usr.password), str)
        self.assertEqual(Usr.password, "")
        self.assertTrue(hasattr(Usr, "first_name"))
        self.assertIs(type(Usr.first_name), str)
        self.assertEqual(Usr.first_name, "")
        self.assertTrue(hasattr(Usr, "last_name"))
        self.assertIs(type(Usr.last_name), str)
        self.assertEqual(Usr.last_name, "")
        self.assertIn("id", Usr.__dict__)
        self.assertTrue(type(Usr.__dict__["id"]), 'str')
        self.assertIn("created_at", Usr.__dict__)
        self.assertTrue(type(Usr.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", Usr.__dict__)
        self.assertTrue(type(Usr.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(Usr.to_dict()["__class__"]), str)
        self.assertIs(type(Usr.to_dict()["id"]), str)
        self.assertIs(type(Usr.to_dict()["created_at"]), str)
        self.assertIs(type(Usr.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of User
         objects"""
        string = "[User] ({}) {}".format(Usr.id, Usr.__dict__)
        self.assertEqual(string, str(Usr))
