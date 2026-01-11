#!/usr/bin/python3
"""Unit tests for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
import os


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_user_inherits_from_base_model(self):
        """Test that User inherits from BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_user_has_email_attr(self):
        """Test that User has email attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertEqual(user.email, "")

    def test_user_has_password_attr(self):
        """Test that User has password attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'password'))
        self.assertEqual(user.password, "")

    def test_user_has_first_name_attr(self):
        """Test that User has first_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertEqual(user.first_name, "")

    def test_user_has_last_name_attr(self):
        """Test that User has last_name attribute"""
        user = User()
        self.assertTrue(hasattr(user, 'last_name'))
        self.assertEqual(user.last_name, "")

    def test_user_attributes_are_strings(self):
        """Test that User attributes are strings"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

    def test_user_id_is_string(self):
        """Test that id is a string"""
        user = User()
        self.assertIsInstance(user.id, str)

    def test_user_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        user = User()
        self.assertIsInstance(user.created_at, datetime)

    def test_user_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        user = User()
        self.assertIsInstance(user.updated_at, datetime)

    def test_user_str_representation(self):
        """Test __str__ method"""
        user = User()
        string = str(user)
        self.assertIn('[User]', string)
        self.assertIn(user.id, string)

    def test_user_to_dict(self):
        """Test User to_dict method"""
        user = User()
        user.email = "test@test.com"
        user.first_name = "John"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@test.com')
        self.assertEqual(user_dict['first_name'], 'John')

    def test_user_save(self):
        """Test User save method"""
        user = User()
        old_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(old_updated_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()