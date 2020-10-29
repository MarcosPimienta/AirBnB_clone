#!/usr/bin/python3
""" Base Model Constructor """

import uuid
from datetime import datetime


class BaseModel:
        """ Base Model Class"""

        def __init__(self):
                """ Constructor """
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        def __str__(self):
                """ Return a printed readable string """

                return "[{}] ({}) {}"\
                        .format(self.__class__.name, self.id, self.__dict__)

        def save(self):
                """  updates the public instance attribute
                        updatedat with the current time """

                self.updated_at = datetime.now()

        def to_dict(self):
