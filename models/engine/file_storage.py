#!/usr/bin/python3
"""
FileStorage module
Handles serialization and deserialization of objects to/from JSON file
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to JSON file and deserializes JSON file to instances
    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary storing all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects

        Returns:
            dict: Dictionary of all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id

        Args:
            obj: Object to add to storage
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserialize the JSON file to __objects
        Only if the JSON file exists
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)

            # Map class names to actual class objects
            class_map = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
            }

            for key, value in obj_dict.items():
                class_name = value['__class__']
                if class_name in class_map:
                    FileStorage.__objects[key] = class_map[class_name](**value)

        except FileNotFoundError:
            pass