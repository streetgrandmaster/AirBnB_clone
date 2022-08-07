#!/usr/bin/python3
"""Unittest cases for Place class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import place
from models.place import Place


class TestPlaceDocs(unittest.TestCase):
    """Tests for Place documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from Place members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.plcfuncs = inspect.getmembers(Place, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.plcfuncs = []

    def test_Place_conforms_pep8(self):
        """Test models/place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testPlace_conforms_pep8(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_place.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(place.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Place class docstring"""
        self.assertTrue(len(Place.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for place functions docstrings"""
        for func in self.plcfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Plc = Place()


class TestPlace(unittest.TestCase):
    """Tests for Place class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(Plc, "city_id"))
        self.assertIs(type(Place.city_id), str)
        self.assertEqual(Plc.city_id, "")
        self.assertTrue(hasattr(Plc, "user_id"))
        self.assertIs(type(Place.user_id), str)
        self.assertEqual(Plc.user_id, "")
        self.assertTrue(hasattr(Plc, "name"))
        self.assertIs(type(Place.name), str)
        self.assertEqual(Plc.name, "")
        self.assertTrue(hasattr(Plc, "description"))
        self.assertIs(type(Place.description), str)
        self.assertEqual(Plc.description, "")
        self.assertTrue(hasattr(Plc, "number_rooms"))
        self.assertIs(type(Place.number_rooms), int)
        self.assertEqual(Plc.number_rooms, 0)
        self.assertTrue(hasattr(Plc, "number_bathrooms"))
        self.assertIs(type(Place.number_bathrooms), int)
        self.assertEqual(Plc.number_bathrooms, 0)
        self.assertTrue(hasattr(Plc, "max_guest"))
        self.assertIs(type(Place.max_guest), int)
        self.assertEqual(Plc.max_guest, 0)
        self.assertTrue(hasattr(Plc, "price_by_night"))
        self.assertIs(type(Place.max_guest), int)
        self.assertEqual(Plc.price_by_night, 0)
        self.assertTrue(hasattr(Plc, "latitude"))
        self.assertIs(type(Place.latitude), float)
        self.assertEqual(Plc.latitude, 0.0)
        self.assertTrue(hasattr(Plc, "longitude"))
        self.assertIs(type(Place.longitude), float)
        self.assertEqual(Plc.longitude, 0.0)
        self.assertTrue(hasattr(Plc, "amenity_ids"))
        self.assertIs(type(Place.amenity_ids), list)
        self.assertEqual(Plc.amenity_ids, [])
        self.assertIn("id", Plc.__dict__)
        self.assertTrue(type(Plc.__dict__["id"]), 'str')
        self.assertIn("created_at", Plc.__dict__)
        self.assertTrue(type(Plc.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", Plc.__dict__)
        self.assertTrue(type(Plc.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(Plc.to_dict()["__class__"]), str)
        self.assertIs(type(Plc.to_dict()["id"]), str)
        self.assertIs(type(Plc.to_dict()["created_at"]), str)
        self.assertIs(type(Plc.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of Place
         objects"""
        string = "[Place] ({}) {}".format(Plc.id, Plc.__dict__)
        self.assertEqual(string, str(Plc))
