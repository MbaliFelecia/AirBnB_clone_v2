#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City  # noqa
from sqlalchemy import Column, String  # noqa
from sqlalchemy.orm import relationship  # noqa


class State(BaseModel, Base):
    """ State class
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
         @property
         def cities(self):
            """Get a list of all related city objects"""
            city_list = []
            for city in list(models.storage.all(city).values()):
                if city.state_id == self.id:
                    city_list.append(city)
                return city_list
