#!/usr/bin/python3
"""Unittest cases for Review class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import review
from models.review import Review


class TestAmenityDocs(unittest.TestCase):
    """Tests for Review documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from Review members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.reviewfuncs = inspect.getmembers(Review, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.reviewfuncs = []

    def test_amenity_conforms_pep8(self):
        """Test models/review.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testamenity_conforms_pep8(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(review.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for Review class docstring"""
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for review functions docstrings"""
        for func in self.reviewfuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


Rvw = Review()


class TestAmenity(unittest.TestCase):
    """Tests for Review class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(Rvw, "place_id"))
        self.assertIs(type(Rvw.place_id), str)
        self.assertEqual(Rvw.place_id, "")
        self.assertTrue(hasattr(Rvw, "user_id"))
        self.assertIs(type(Rvw.user_id), str)
        self.assertEqual(Rvw.user_id, "")
        self.assertTrue(hasattr(Rvw, "text"))
        self.assertIs(type(Rvw.text), str)
        self.assertEqual(Rvw.text, "")
        self.assertIn("id", Rvw.__dict__)
        self.assertTrue(type(Rvw.__dict__["id"]), 'str')
        self.assertIn("created_at", Rvw.__dict__)
        self.assertTrue(type(Rvw.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", Rvw.__dict__)
        self.assertTrue(type(Rvw.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(Rvw.to_dict()["__class__"]), str)
        self.assertIs(type(Rvw.to_dict()["id"]), str)
        self.assertIs(type(Rvw.to_dict()["created_at"]), str)
        self.assertIs(type(Rvw.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of Review
         objects"""
        string = "[Review] ({}) {}".format(Rvw.id, Rvw.__dict__)
        self.assertEqual(string, str(Rvw))
