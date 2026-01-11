#!/usr/bin/python3
"""Unit tests for FileStorage."""
import os
import json
import unittest
from unittest.mock import patch

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class."""

    def setUp(self):
        """Set up test environment."""

        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test."""

        try:
            os.remove("test_file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_docstring(self):
        """Test that FileStorage class is documented."""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_file_path_attribute_exists(self):
        """Test __file_path private class attribute exists."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))

    def test_objects_attribute_exists(self):
        """Test __objects private class attribute exists."""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

    def test_all_returns_dict(self):
        """Test all() returns a dictionary."""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_new_adds_object(self):
        """Test new() adds an object with correct key format."""
        storage = FileStorage()
        bm = BaseModel()
        key = f"BaseModel.{bm.id}"
        storage.new(bm)
        self.assertIn(key, storage.all())

    def test_save_creates_file(self):
        """Test save() creates a JSON file and writes serialized objects."""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)

        with patch.object(FileStorage, "_FileStorage__file_path", "test_file.json"):
            storage.save()
            self.assertTrue(os.path.exists("test_file.json"))

            with open("test_file.json", "r", encoding="utf-8") as f:
                data = json.load(f)

            self.assertIn(f"BaseModel.{bm.id}", data)
            self.assertEqual(data[f"BaseModel.{bm.id}"]["__class__"], "BaseModel")

    def test_reload_does_nothing_if_file_missing(self):
        """Test reload() does not raise if file doesn't exist."""
        storage = FileStorage()
        with patch.object(FileStorage, "_FileStorage__file_path", "test_file.json"):

            try:
                os.remove("test_file.json")
            except FileNotFoundError:
                pass
            storage.reload()  # Should not raise
            self.assertEqual(len(storage.all()), 0)

    def test_reload_restores_objects(self):
        """Test reload() restores objects from file."""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)

        with patch.object(FileStorage, "_FileStorage__file_path", "test_file.json"):
            storage.save()

            FileStorage._FileStorage__objects = {}
            storage.reload()

            key = f"BaseModel.{bm.id}"
            self.assertIn(key, storage.all())
            self.assertIsInstance(storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()