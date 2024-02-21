#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import *
from models import HBNB_TYPE_STORAGE
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade='all, delete-orphan')

    if HBNB_TYPE_STORAGE == 'db':
        @property
        def cities(self):
            from models import storage
            dec = storage.all(City)
            out = []
            for k, city in dec:
                if city.state_id == self.id:
                    out.append(city)
            return out
