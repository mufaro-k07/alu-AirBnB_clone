#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
import os


class TestState(unittest.TestCase):
    """Test cases for State class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_state_inherits_from_base_model(self):
        """Test that State inherits from BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)

    def test_state_has_name_attr(self):
        """Test that State has name attribute"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_state_name_is_string(self):
        """Test that name is a string"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_id_is_string(self):
        """Test that id is a string"""
        state = State()
        self.assertIsInstance(state.id, str)

    def test_state_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        state = State()
        self.assertIsInstance(state.created_at, datetime)

    def test_state_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        state = State()
        self.assertIsInstance(state.updated_at, datetime)

    def test_state_str_representation(self):
        """Test __str__ method"""
        state = State()
        string = str(state)
        self.assertIn('[State]', string)
        self.assertIn(state.id, string)

    def test_state_to_dict(self):
        """Test State to_dict method"""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'California')

    def test_state_save(self):
        """Test State save method"""
        state = State()
        old_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(old_updated_at, state.updated_at)


if __name__ == '__main__':
    unittest.main()