#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker, scoped_session


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

        classes = {
            'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
            }

        Session = sessionmaker()
        self.__session = Session()

        ret = {}

        if type(cls) is not str:
            cls = cls.__name__
        if cls:
            for obj in self.__session.query(classes[cls]):
                ret[cls + '.' + obj.id] = obj
        else:
            for k in classes.keys():
                for obj in self.__session.query(classes[k]):
                    ret[k + '.' + obj.id] = obj
        return ret

    def new(self, obj):
        """add a new object to the data base"""
        self.__session.add(obj)

    def save(self):
        """commit all change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object if not null"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """reload all the objets"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        ses = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(ses)

    def close(self):
        """Closes the session"""
        self.__session.close()
