#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *


class Amenity(BaseModel, Base):
    name = name = Column(String(128), nullable=False)
