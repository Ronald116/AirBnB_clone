#!/usr/bin/python3
"""A class FileStorage that serializes and deserializes"""

import json
import datetime
from os.path import exists


class FileStorage:
    """
    a class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """eturns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        k = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[k] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file to __objects (if it exists)."""
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key]['created_at'] = datetime.strptime(
                        obj_dict[key]['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict[key]['updated_at'] = datetime.strptime(
                        obj_dict[key]['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                    module_name = class_name.lower()
                    module = __import__('models.' + module_name,
                                        globals(), locals(), [class_name], 0)
                    class_ = getattr(module, class_name)
                    instance = class_(**value)
                    self.__objects[key] = instance

