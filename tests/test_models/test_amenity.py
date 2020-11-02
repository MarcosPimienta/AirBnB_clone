#!/usr/bin/python3
"""Unittest for Amenity"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unittest for Amenity"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_amenity = Amenity()
        self.assertTrue(isinstance(my_amenity, BaseModel))
        self.assertTrue(type(my_amenity), Amenity)
        self.assertEqual(my_amenity.name, "")
        self.assertIsNotNone(my_amenity.id)
        self.assertIsNotNone(my_amenity.created_at)
        self.assertIsNotNone(my_amenity.updated_at)
        self.assertTrue(type(my_amenity.created_at), datetime)
        self.assertTrue(type(my_amenity.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        amenity2 = Amenity()
        expected = "[{}] ({}) {}\n".format(amenity2.__class__.__name__,
                                           amenity2.id, amenity2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(amenity2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        amenity3 = Amenity()
        updated_0 = amenity3.updated_at
        amenity3.save()
        updated_1 = amenity3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        amenity4 = Amenity()
        d = amenity4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "Amenity")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
