#!/usr/bin/python3
"""Unittest for BaseModel"""
import unittest
import contextlib
import models
import os
from io import StringIO
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Unittest for BaseModel"""

    def test_doc(self):
        """Test docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        """Test Initialize method"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        self.assertTrue(type(my_model.created_at), datetime)
        self.assertTrue(type(my_model.updated_at), datetime)

        dc = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
              'created_at': '2017-09-28T21:03:54.052298',
              '__class__': 'BaseModel', 'my_number': 89,
              'updated_at': '2017-09-28T21:03:54.052302', 'name': 'Holberton'}
        basemod = BaseModel(**dc)
        self.assertTrue(isinstance(basemod, BaseModel))
        self.assertEqual(basemod.name, "Holberton")
        self.assertEqual(basemod.my_number, 89)
        self.assertIsNotNone(basemod.id)
        self.assertEqual(basemod.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsNotNone(basemod.created_at)
        self.assertIsNotNone(basemod.updated_at)
        self.assertTrue(type(basemod.created_at), datetime)
        self.assertTrue(type(basemod.updated_at), datetime)

    def test_str(self):
        """Test str method"""
        my_model2 = BaseModel()
        expected = "[{}] ({}) {}\n".format(my_model2.__class__.__name__,
                                           my_model2.id, my_model2.__dict__)
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(my_model2)
            self.assertEqual(buf.getvalue(), expected)

    def test_save(self):
        """Test save method"""
        model3 = BaseModel()
        updated_0 = model3.updated_at
        model3.save()
        updated_1 = model3.updated_at
        self.assertNotEqual(updated_0, updated_1)
        self.assertTrue(os.path.isfile("file.json"))

    def test_todict(self):
        """Test to_dict method"""
        model_4 = BaseModel()
        d = model_4.to_dict()
        self.assertTrue("__class__" in d)
        self.assertTrue(d["__class__"], "BaseModel")
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
