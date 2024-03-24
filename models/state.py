#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from models import *

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade='all, delete-orphan')
    
    if HBNB_TYPE_STORAGE != 'db':
        @property
        def cities():
            all_cities = []
            cts = storage.all(City)
            for k, c in cts:
                if c.state_id == self.id:
                    all_cities.append(c)
            return all_cities
