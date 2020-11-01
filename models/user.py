#!/usr/bin/python3
"""  Class User that inherits from BaseModel """

from models.base_model import BaseModel


class User(BaseModel):
        """  User Class """

        email = ""
        password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
                """  Initializes data """

                super().__init__(*args, **kwargs)
