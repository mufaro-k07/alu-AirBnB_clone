#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import os


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_inherits_from_base_model(self):
        """Test that Amenity inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_has_name_attr(self):
        """Test that Amenity has name attribute"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_amenity_name_is_string(self):
        """Test that name is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_id_is_string(self):
        """Test that id is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_amenity_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_str_representation(self):
        """Test __str__ method"""
        amenity = Amenity()
        string = str(amenity)
        self.assertIn('[Amenity]', string)
        self.assertIn(amenity.id, string)

    def test_amenity_to_dict(self):
        """Test Amenity to_dict method"""
        amenity = Amenity()
        amenity.name = "WiFi"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'WiFi')

    def test_amenity_save(self):
        """Test Amenity save method"""
        amenity = Amenity()
        old_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(old_updated_at, amenity.updated_at)


if __name__ == '__main__':
    unittest.main()