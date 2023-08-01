#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """Placeholder"""
    __engine = None
    __session = None

    def __init__(self):
        """instantiation"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb:\
                        //{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop(self.__engine)

    def all(self, cls=None):
        """Returns a dict of the specified cls"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Session = sessionmaker()
        self.__session = Session()
        if cls is None:
            
