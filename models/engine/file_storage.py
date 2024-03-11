#!/usr/bin/python3
"""Modeule defines 'FileStorage class'"""
import json
from os import path


class FileStorage():
    """Serializes instances to a JSON file and deserializes
    JSON file to instances.
    """
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self, obj=None):
        """serializes _objects to the JSON file"""
        #handling dynamic attriibutes
        if obj is not None:
            key2 = "{}.{}".format(obj.__class__.__name__, obj.id)
            for key, value in obj.__dict__.items():
                if key not in self.__objects[key2]:
                    self.__objects[key2][key] = value

        with open(self.__file_path, mode='w', encoding='utf-8') as myFile:
            myFile.write(json.dumps(self.__objects))

    def reload(self):
        """deserializes __objects to the JSON file"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as myFile:
               self.__objects = json.loads(myFile.read())
