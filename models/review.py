#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel

    Public class attributes:
        place_id (str): Place ID
        user_id (str): User ID
        text (str): Review text
    """
    place_id = ""
    user_id = ""
    text = ""