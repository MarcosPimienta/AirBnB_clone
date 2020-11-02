#!/usr/bin/python3
"""Unittest for Place"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Unittest for Place"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(Place.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))
        self.assertTrue(type(my_place), Place)
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])
        self.assertIsNotNone(my_place.id)
        self.assertIsNotNone(my_place.created_at)
        self.assertIsNotNone(my_place.updated_at)
        self.assertTrue(type(my_place.created_at), datetime)
        self.assertTrue(type(my_place.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        place2 = Place()
        expected = "[{}] ({}) {}\n".format(place2.__class__.__name__,
                                           place2.id, place2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(place2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        place3 = Place()
        updated_0 = place3.updated_at
        place3.save()
        updated_1 = place3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        place4 = Place()
        d = place4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "Place")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
