#!/usr/bin/env python3
""" State Module for HBNB project """
from models.base_model import *


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", backref="state", cascade='all, delete-orphan')

    @property
    def cities(self):
        from models import storage
        dec = storage.all()
        out = []
        for k, city in dec:
            if k.split('.')[0] == 'City':
                if city.state_id == self.id:
                    out.append(city)
        return out
