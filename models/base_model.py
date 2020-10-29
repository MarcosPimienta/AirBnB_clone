#!/usr/bin/python3
""" Base Model Constructor """

import uuid
from datetime import datetime


class BaseModel:
        """ Base Model Class"""

        def __init__(self, *args, **kwargs):
                """ Constructor """
                fmt = "%Y-%m-%dT%H:%M:%S.%f"
                if kwargs:
                        if "__class__" in kwargs.keys():
                                kwargs.pop("__class__")
                        if "created_at" in kwargs.keys() and type(kwargs["created_at"]) is str:
                                kwargs["created_at"] = datetime.strptime(kwargs["created_at"], fmt)
                        if "updated_at" in kwargs.keys() and type(kwargs["updated_at"]) is str:
                                kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], fmt)
                        self.__dict__.update(kwargs)
                else:
                        self.id = str(uuid.uuid4())
                        self.created_at = datetime.now()
                        self.updated_at = datetime.now()

        def __str__(self):
                """ Return a printed readable string """

                return "[{}] ({}) {}".format(self.__class__.__name__,
                                             self.id, self.__dict__)

        def save(self):
                """  updates the public instance attribute
                        updatedat with the current time """

                self.updated_at = datetime.now()

        def to_dict(self):
                """returns a dictionary containing all keys/values of
                dict of the instance"""
                fmt = "%Y-%m-%dT%H:%M:%S.%f"
                d = self.__dict__.copy()
                d["__class__"] = self.__class__.__name__
                d["created_at"] = d["created_at"].strftime(fmt)
                d["updated_at"] = d["updated_at"].strftime(fmt)
                return d
