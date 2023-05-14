#!/usr/bin/python3
"""This creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class that manages review objects"""

    place_id = ""
    user_id = ""
    text = ""
