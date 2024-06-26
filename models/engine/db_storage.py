#!/usr/bin/python3
"""This Module contains the Database Storage"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.state import State
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Engine for the Database"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initialization """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True
        )

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query for objects on current session"""
        classes = {
            "City": City,
            "State": State,
            "User": User,
        }
        result = {}
        query_row = []

        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query_row = self.__session.query(cls)
            for obj in query_row:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
            return result
        else:
            for name, val in classes.items():
                query_row = self.__session.query(val)
                for obj in query_row:
                    key = "{}.{}".format(name, obj.id)
                    result[key] = obj
            return result

    def new(self, obj):
        """Adds object to current session"""
        self.__session.add(obj)

    def save(self):
        """Saves changes to session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current session"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates all tables in the database
        Creates all database session from Engine
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

