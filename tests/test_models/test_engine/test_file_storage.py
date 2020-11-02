#!/usr/bin/python3
"""Unittest for FileStorage"""
import unittest
import contextlib
import models
import os
import json
from io import StringIO
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from datetime import datetime

class TestFileStorage(unittest.TestCase):
    """Unittest for FileStorage"""

    def test_all(self):
        """Test all method"""
        d = models.storage.all()
        self.assertTrue(type(d), dict)

    def test_new(self):
        """Test new method"""
        user1 = User()
        models.storage.new(user1)
        k = "{}.{}".format(user1.__class__.__name__, user1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(user1 in models.storage.all().values())

        am1 = Amenity()
        models.storage.new(am1)
        k = "{}.{}".format(am1.__class__.__name__, am1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(am1 in models.storage.all().values())

        ct1 = City()
        models.storage.new(ct1)
        k = "{}.{}".format(ct1.__class__.__name__, ct1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(ct1 in models.storage.all().values())

        bs1 = BaseModel()
        models.storage.new(bs1)
        k = "{}.{}".format(bs1.__class__.__name__, bs1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(bs1 in models.storage.all().values())

        st1 = State()
        models.storage.new(st1)
        k = "{}.{}".format(st1.__class__.__name__, st1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(st1 in models.storage.all().values())

        plc = Place()
        models.storage.new(plc)
        k = "{}.{}".format(plc.__class__.__name__, plc.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(plc in models.storage.all().values())

        rv1 = Review()
        models.storage.new(rv1)
        k = "{}.{}".format(rv1.__class__.__name__, rv1.id)
        self.assertTrue(k in models.storage.all())
        self.assertTrue(rv1 in models.storage.all().values())

    def test_save(self):
        """Test save method"""
        new_usr = User()
        models.storage.new(new_usr)
        models.storage.save()
        k1 = "{}.{}".format(new_usr.__class__.__name__, new_usr.id)

        new_am = Amenity()
        models.storage.new(new_am)
        models.storage.save()
        k2 = "{}.{}".format(new_am.__class__.__name__, new_am.id)

        new_ct = City()
        models.storage.new(new_ct)
        models.storage.save()
        k3 = "{}.{}".format(new_ct.__class__.__name__, new_ct.id)

        new_bs = BaseModel()
        models.storage.new(new_bs)
        models.storage.save()
        k4 = "{}.{}".format(new_bs.__class__.__name__, new_bs.id)

        new_st = State()
        models.storage.new(new_st)
        models.storage.save()
        k5 = "{}.{}".format(new_st.__class__.__name__, new_st.id)

        new_plc = Place()
        models.storage.new(new_plc)
        models.storage.save()
        k6 = "{}.{}".format(new_plc.__class__.__name__, new_plc.id)

        new_rv = Review()
        models.storage.new(new_rv)
        models.storage.save()
        k7 = "{}.{}".format(new_rv.__class__.__name__, new_rv.id)

        with open("file.json", encoding="utf-8") as f:
            content = json.load(f)
        self.assertTrue(k1 in content)
        self.assertTrue(k2 in content)
        self.assertTrue(k3 in content)
        self.assertTrue(k4 in content)
        self.assertTrue(k5 in content)
        self.assertTrue(k6 in content)
        self.assertTrue(k7 in content)

    def test_reload(self):
        """Test reload method"""
        models.storage.reload()
        self.assertIsNotNone(models.storage.all())
        self.assertTrue(type(models.storage.all()), dict)
