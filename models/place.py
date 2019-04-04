#!/usr/bin/python3
"""This is the place class"""
import os
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place",
                           cascade="all, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """
        returns a list of reviews with place ids
        """
        reviews = models.storage.all("Review").values()
        return [r for r in reviews if r.place_id == self.id]

    if os.getenv("HBNB_TYPE_STORAGE") == "fs":
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """
            returns a list of amenities with amenity ids
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """
            setter for amenities
            """
            if type(obj) is Amenity:
                self.amenity_ids.append(obj.id)
