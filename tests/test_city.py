#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import os


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_city_inherits_from_base_model(self):
        """Test that City inherits from BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_city_has_state_id_attr(self):
        """Test that City has state_id attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertEqual(city.state_id, "")

    def test_city_has_name_attr(self):
        """Test that City has name attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.name, "")

    def test_city_attributes_are_strings(self):
        """Test that City attributes are strings"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_id_is_string(self):
        """Test that id is a string"""
        city = City()
        self.assertIsInstance(city.id, str)

    def test_city_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_city_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_city_str_representation(self):
        """Test __str__ method"""
        city = City()
        string = str(city)
        self.assertIn('[City]', string)
        self.assertIn(city.id, string)

    def test_city_to_dict(self):
        """Test City to_dict method"""
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA"
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'San Francisco')
        self.assertEqual(city_dict['state_id'], 'CA')

    def test_city_save(self):
        """Test City save method"""
        city = City()
        old_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(old_updated_at, city.updated_at)


if __name__ == '__main__':
    unittest.main()