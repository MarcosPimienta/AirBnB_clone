#!/usr/bin/python3
""" Base Model Constructor """

import uuid
from datetime import datetime


class BaseModel:
        """ Base Model Class"""

        def __init__(self, *args, **kg):
                """ Constructor """
                fmt = "%Y-%m-%dT%H:%M:%S.%f"
                if kg:
                        if "__class__" in kg.keys():
                                kg.pop("__class__")
                        if "created_at" in kg.keys()\
                           and type(kg["created_at"]) is str:
                                kg["created_at"] = datetime.\
                                                   strptime(kg["created_at"],
                                                            fmt)
                        if "updated_at" in kg.keys()\
                           and type(kg["updated_at"]) is str:
                                kg["updated_at"] = datetime.\
                                                   strptime(kg["updated_at"],
                                                            fmt)
                        self.__dict__.update(kg)
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
