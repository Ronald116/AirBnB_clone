#!/usr/bin/python3
"""This is the base model class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """A BaseModel class which other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """
            Initializes instance attribute
        
            Args:
                - *args: lists of arguments
                - **kwargs: list s of keyword arguments
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                            kwargs[value], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                            kwargs[value], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[value]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)



    def __str__(self):
        """Returns string representation of instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict


    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()
        

