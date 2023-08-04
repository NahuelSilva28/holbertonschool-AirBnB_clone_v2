#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from os import getenv
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref='place')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="places", viewonly=False)
    else:
        @property
        def reviews(self):
            """Returns the list of Review instances
            with place_id equals to the current Place.id"""
            from models.review import Review
            from models import storage
            listed = []
            for k, v in storage.all(Review):
                if v["place_id"] == self.id:
                    listed.append(v)
            return listed

        @property
        def amenities(self):
            """Returns the list of Amenity instances
            with place_id equals to the current Amenity.id"""
            from models.amenity import Amenity
            from models import storage
            listed = []
            for k, v in storage.all(Amenity):
                if v["place_id"] == self.id:
                    listed.append(v)
            return listed

        @ amenities.setter
        def amenities(self, append):
            """ Setter attribute amenities """

            if type(append).__name__ == "Amenity":
                self.amenity_ids.append(append.id)
