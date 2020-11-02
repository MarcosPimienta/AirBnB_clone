#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(Review.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_review = Review()
        self.assertTrue(isinstance(my_review, BaseModel))
        self.assertTrue(type(my_review), Review)
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")
        self.assertIsNotNone(my_review.id)
        self.assertIsNotNone(my_review.created_at)
        self.assertIsNotNone(my_review.updated_at)
        self.assertTrue(type(my_review.created_at), datetime)
        self.assertTrue(type(my_review.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        review2 = Review()
        expected = "[{}] ({}) {}\n".format(review2.__class__.__name__,
                                           review2.id, review2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(review2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        review3 = Review()
        updated_0 = review3.updated_at
        review3.save()
        updated_1 = review3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        review4 = Review()
        d = review4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "Review")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
