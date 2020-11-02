#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))
        self.assertTrue(type(my_city), City)
        self.assertEqual(my_city.name, "")
        self.assertEqual(my_city.state_id, "")
        self.assertIsNotNone(my_city.id)
        self.assertIsNotNone(my_city.created_at)
        self.assertIsNotNone(my_city.updated_at)
        self.assertTrue(type(my_city.created_at), datetime)
        self.assertTrue(type(my_city.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        city2 = City()
        expected = "[{}] ({}) {}\n".format(city2.__class__.__name__,
                                           city2.id, city2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(city2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        city3 = City()
        updated_0 = city3.updated_at
        city3.save()
        updated_1 = city3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        city4 = City()
        d = city4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "City")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
