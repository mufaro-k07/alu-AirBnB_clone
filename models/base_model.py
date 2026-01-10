#!/usr/bin/python3
"""
BaseModel module
Define the BaseModel class
"""

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """BaseModel class defines all common attributes for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialises a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at, updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        """Update updated_at and saves the instance"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict