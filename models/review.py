#!/usr/bin/python3
"""class Review that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """defines a class review"""
    place_id = ""
    user_id = ""
    text = ""
