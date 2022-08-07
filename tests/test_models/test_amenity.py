#!/usr/bin/python3
"""Unittest cases for Amenity class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import amenity
from models.amenity import Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests for Amenity documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from Amenity members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.amenityfuncs = inspect.getmembers(Amenity, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.amenityfuncs = []

    def test_amenity_conforms_pep8(self):
        """Test models/amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testamenity_conforms_pep8(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(amenity.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Amenity class docstring"""
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for amenity functions docstrings"""
        for func in self.amenityfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Amn = Amenity()


class TestAmenity(unittest.TestCase):
    """Tests for Amenity class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(Amn, "name"))
        self.assertIs(type(Amn.name), str)
        self.assertEqual(Amn.name, "")
        self.assertIn("id", Amn.__dict__)
        self.assertTrue(type(Amn.__dict__["id"]), 'str')
        self.assertIn("created_at", Amn.__dict__)
        self.assertTrue(type(Amn.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", Amn.__dict__)
        self.assertTrue(type(Amn.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(Amn.to_dict()["__class__"]), str)
        self.assertIs(type(Amn.to_dict()["id"]), str)
        self.assertIs(type(Amn.to_dict()["created_at"]), str)
        self.assertIs(type(Amn.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of Amenity
         objects"""
        string = "[Amenity] ({}) {}".format(Amn.id, Amn.__dict__)
        self.assertEqual(string, str(Amn))
