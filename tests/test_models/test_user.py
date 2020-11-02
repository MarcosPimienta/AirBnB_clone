#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(User.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))
        self.assertTrue(type(my_user), User)
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")
        self.assertIsNotNone(my_user.id)
        self.assertIsNotNone(my_user.created_at)
        self.assertIsNotNone(my_user.updated_at)
        self.assertTrue(type(my_user.created_at), datetime)
        self.assertTrue(type(my_user.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        user2 = User()
        expected = "[{}] ({}) {}\n".format(user2.__class__.__name__,
                                           user2.id, user2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(user2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        user3 = User()
        updated_0 = user3.updated_at
        user3.save()
        updated_1 = user3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        user4 = User()
        d = user4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "User")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
