#!/usr/bin/python3
""" Module for FileStorage class"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file
    to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesnt exist, no exception should be raised)"""
        d = {"BaseModel": BaseModel, "User": User}
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                k_obj = json.load(f)
                for k in k_obj:
                    self.__objects[k] = d[k_obj[k]["__class__"]](**k_obj[k])
        except:
            pass
