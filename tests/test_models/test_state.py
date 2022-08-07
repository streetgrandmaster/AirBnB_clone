#!/usr/bin/python3
"""Unittest cases for State class"""
import inspect
import pep8
import unittest
from models.base_model import BaseModel
from models import state
from models.state import State


class TestStateDocs(unittest.TestCase):
    """Tests for State documentation"""
    @classmethod
    def setUpClass(cls):
        """Makes sure all prerequisites for our tests are available"""

        """gives only members from State members, in a list,
         which have true values for our predicate(2nd arg)"""
        cls.statefuncs = inspect.getmembers(State, inspect.isfunction)

    @classmethod
    def tearDownClass(cls):
        """Cleans all those prerequisites"""
        cls.statefuncs = []

    def test_State_conforms_pep8(self):
        """Test models/state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_testState_conforms_pep8(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 0, "Not to pep8 standard")

    def test_module_docstr(self):
        """Tests for the module docstring"""
        self.assertTrue(len(state.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for State class docstring"""
        self.assertTrue(len(State.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for state functions docstrings"""
        for func in self.statefuncs:
            self.assertTrue(len(func[1].__doc__) >= 1)


St = State()


class TestState(unittest.TestCase):
    """Tests for State class"""
    def test_init(self):
        """Tests proper initialization method"""
        self.assertTrue(hasattr(St, "name"))
        self.assertIs(type(St.name), str)
        self.assertEqual(St.name, "")
        self.assertIn("id", St.__dict__)
        self.assertTrue(type(St.__dict__["id"]), 'str')
        self.assertIn("created_at", St.__dict__)
        self.assertTrue(type(St.__dict__["created_at"]), 'datetime')
        self.assertIn("updated_at", St.__dict__)
        self.assertTrue(type(St.__dict__["updated_at"]), 'datetime')

    def test_to_dict(self):
        """Tests 'to_dict' returns a dictionary containing correct
         keys/values of __dict__ of the instance (json)"""
        self.assertIs(type(St.to_dict()["__class__"]), str)
        self.assertIs(type(St.to_dict()["id"]), str)
        self.assertIs(type(St.to_dict()["created_at"]), str)
        self.assertIs(type(St.to_dict()["updated_at"]), str)

    def test_str(self):
        """Tests'str' returns the informal representation of State
         objects"""
        string = "[State] ({}) {}".format(St.id, St.__dict__)
        self.assertEqual(string, str(St))
