#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from hashlib import md5

classes = {"Amenity": "Amenity", "BaseModel": "BaseModel", "City": "City",
           "Place": "Place", "Review": "Review", "State": "State", "User": "User"}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            # Lazy import to prevent circular import
            from models import storage
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    # ... rest of the methods remain unchanged ...

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        # Lazy import to prevent circular import
        from models import storage
        if cls not in classes.values():
            return None

        all_cls = storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        # Lazy import to prevent circular import
        from models import storage
        all_class = [storage.classes[key] for key in classes]

        if not cls:
            count = 0
            for clas in all_class:
                count += len(storage.all(clas).values())
        else:
            count = len(storage.all(cls).values())

        return count
