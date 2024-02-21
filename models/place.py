#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import *
from models import HBNB_TYPE_STORAGE
from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                     Column('place_id', String(60),
                            ForeignKey('places.id'),
                            primary_key=True,
                            nullable=False),
                     Column('amenity_id', String(60),
                            ForeignKey('amenities.id'),
                            primary_key=True,
                            nullable=False))


class Place(BaseModel, Base):
       """ A place to stay """
       __tablename__ = 'places'
       city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
       user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
       name = Column(String(128), nullable=False)
       description =Column(String(1024))
       number_rooms = Column(Integer, default=0, nullable=False)
       number_bathrooms = Column(Integer, default=0, nullable=False)
       max_guest = Column(Integer, default=0, nullable=False)
       price_by_night = Column(Integer, default=0, nullable=False)
       latitude = Column(Float)
       longitude = Column(Float)
       reviews = relationship('Review', backref='place', cascade='delete')
       amenities = relationship('Amenity', secondary='place_amenity', viewonly=False,
                                   backref='place_amenities')
       amenity_ids = []
       if HBNB_TYPE_STORAGE == 'db':
              @property
              def reviews(self):
                     from models import storage
                     dec = storage.all(Review)
                     out = []
                     for k, review in dec:
                            if review.place_id == self.id:
                                   out.append(review)
                     return out
