#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    Public class attributes:
        state_id (str): State ID
        name (str): Name of the city
    """
    state_id = ""
    name = ""