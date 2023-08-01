#!/usr/bin/python3
""" Stte Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City instances
        with state_id equals to the current State.id"""
        from models.city import City
        from models import storage
        listed = []
        for k, v in storage.all(City):
            if v["state_id"] == self.id:
                listed.append(v)
        return listed
