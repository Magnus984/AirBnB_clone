#!/usr/bin/python3
"""Module that defines BaseModel class."""
import uuid
from datetime import datetime
from models import storage

class BaseModel():
    """Defines all common attributes/methods for other classes"""

    def __init__(self, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)


    def __str__(self):
        print("Calling __str__...")
        string = "[" + str(self.__class__.__name__) + "]"
        string += " (" + self.id + ") "
        string += str(self.__dict__)
        return string

    def save(self):
        """Updates the public instance attribute 'updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        storage.save(self)
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of
        '__dict__' of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        for key, value in dict_copy.items():
            if isinstance(value, datetime):
                dict_copy[key] = value.isoformat()
        return dict_copy
