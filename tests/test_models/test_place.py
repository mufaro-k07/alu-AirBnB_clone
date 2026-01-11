#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
import os


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_place_inherits_from_base_model(self):
        """Test that Place inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_place_has_city_id_attr(self):
        """Test that Place has city_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertEqual(place.city_id, "")

    def test_place_has_user_id_attr(self):
        """Test that Place has user_id attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertEqual(place.user_id, "")

    def test_place_has_name_attr(self):
        """Test that Place has name attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'name'))
        self.assertEqual(place.name, "")

    def test_place_has_description_attr(self):
        """Test that Place has description attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'description'))
        self.assertEqual(place.description, "")

    def test_place_has_number_rooms_attr(self):
        """Test that Place has number_rooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertEqual(place.number_rooms, 0)

    def test_place_has_number_bathrooms_attr(self):
        """Test that Place has number_bathrooms attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertEqual(place.number_bathrooms, 0)

    def test_place_has_max_guest_attr(self):
        """Test that Place has max_guest attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertEqual(place.max_guest, 0)

    def test_place_has_price_by_night_attr(self):
        """Test that Place has price_by_night attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertEqual(place.price_by_night, 0)

    def test_place_has_latitude_attr(self):
        """Test that Place has latitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertEqual(place.latitude, 0.0)

    def test_place_has_longitude_attr(self):
        """Test that Place has longitude attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertEqual(place.longitude, 0.0)

    def test_place_has_amenity_ids_attr(self):
        """Test that Place has amenity_ids attribute"""
        place = Place()
        self.assertTrue(hasattr(place, 'amenity_ids'))
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_types(self):
        """Test that Place attributes have correct types"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)

    def test_place_str_representation(self):
        """Test __str__ method"""
        place = Place()
        string = str(place)
        self.assertIn('[Place]', string)
        self.assertIn(place.id, string)

    def test_place_to_dict(self):
        """Test Place to_dict method"""
        place = Place()
        place.name = "Lovely place"
        place.number_rooms = 3
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], 'Lovely place')
        self.assertEqual(place_dict['number_rooms'], 3)

    def test_place_save(self):
        """Test Place save method"""
        place = Place()
        old_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(old_updated_at, place.updated_at)


if __name__ == '__main__':
    unittest.main()