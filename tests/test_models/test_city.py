#!/usr/bin/python3
"""Unittest cases for City class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import city
from models.city import City


class TestAmenityDocs(unittest.TestCase):
    """Tests for City documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from City members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.cityfuncs = inspect.getmembers(City, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.cityfuncs = []

    def test_amenity_conforms_pep8(self):
        """Test models/city.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testamenity_conforms_pep8(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(city.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for City class docstring"""
        self.assertTrue(len(City.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for city functions docstrings"""
        for func in self.cityfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Ct = City()


class TestAmenity(unittest.TestCase):
    """Tests for City class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(Ct, "state_id"))
        self.assertIs(type(Ct.state_id), str)
        self.assertEqual(Ct.state_id, "")
        self.assertTrue(hasattr(Ct, "name"))
        self.assertIs(type(Ct.name), str)
        self.assertEqual(Ct.name, "")
        self.assertIn("id", Ct.__dict__)
        self.assertTrue(type(Ct.__dict__["id"]), 'str')
        self.assertIn("created_at", Ct.__dict__)
        self.assertTrue(type(Ct.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", Ct.__dict__)
        self.assertTrue(type(Ct.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(Ct.to_dict()["__class__"]), str)
        self.assertIs(type(Ct.to_dict()["id"]), str)
        self.assertIs(type(Ct.to_dict()["created_at"]), str)
        self.assertIs(type(Ct.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of City
         objects"""
        string = "[City] ({}) {}".format(Ct.id, Ct.__dict__)
        self.assertEqual(string, str(Ct))
