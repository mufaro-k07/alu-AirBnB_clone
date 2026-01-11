#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime
import os


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def setUp(self):
        """Set up test environment"""
        pass

    def tearDown(self):
        """Clean up after tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_review_inherits_from_base_model(self):
        """Test that Review inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_review_has_place_id_attr(self):
        """Test that Review has place_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertEqual(review.place_id, "")

    def test_review_has_user_id_attr(self):
        """Test that Review has user_id attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertEqual(review.user_id, "")

    def test_review_has_text_attr(self):
        """Test that Review has text attribute"""
        review = Review()
        self.assertTrue(hasattr(review, 'text'))
        self.assertEqual(review.text, "")

    def test_review_attributes_are_strings(self):
        """Test that Review attributes are strings"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_id_is_string(self):
        """Test that id is a string"""
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_review_created_at_is_datetime(self):
        """Test that created_at is datetime"""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_review_updated_at_is_datetime(self):
        """Test that updated_at is datetime"""
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_review_str_representation(self):
        """Test __str__ method"""
        review = Review()
        string = str(review)
        self.assertIn('[Review]', string)
        self.assertIn(review.id, string)

    def test_review_to_dict(self):
        """Test Review to_dict method"""
        review = Review()
        review.text = "Great place!"
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['text'], 'Great place!')

    def test_review_save(self):
        """Test Review save method"""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(old_updated_at, review.updated_at)


if __name__ == '__main__':
    unittest.main()