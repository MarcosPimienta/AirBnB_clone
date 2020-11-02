#!/usr/bin/python3
"""Unittest for State"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittest for State"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(State.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))
        self.assertTrue(type(my_state), State)
        self.assertEqual(my_state.name, "")
        self.assertIsNotNone(my_state.id)
        self.assertIsNotNone(my_state.created_at)
        self.assertIsNotNone(my_state.updated_at)
        self.assertTrue(type(my_state.created_at), datetime)
        self.assertTrue(type(my_state.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        state2 = State()
        expected = "[{}] ({}) {}\n".format(state2.__class__.__name__,
                                           state2.id, state2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(state2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        state3 = State()
        updated_0 = state3.updated_at
        state3.save()
        updated_1 = state3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        state4 = State()
        d = state4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "State")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
