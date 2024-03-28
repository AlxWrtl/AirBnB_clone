#!/usr/bin/python3
"""DB Storage Engine Module"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import sqlalchemy

classes = {'User': User, 'State': State, 'City': City,
           'Amenity': Amenity, 'Place': Place, 'Review': Review}


class DBStorage:
    """DB Storage Engine Class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        # Get MySQL configuration from environment variables
        HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
        HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
        HBNB_ENV = getenv("HBNB_ENV")

        # Create the database engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(HBNB_MYSQL_USER,
                                              HBNB_MYSQL_PWD,
                                              HBNB_MYSQL_HOST,
                                              HBNB_MYSQL_DB),
                                      pool_pre_ping=True)
        # Drop all tables if environment is 'test'
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects by class name, or all if cls=None"""

        # Define a class map similar to the first snippet
        class_map = {
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

        # Query objects dictionary
        objects = {}

        # Iterate over the classes in the class_map
        for class_name, class_obj in class_map.items():
            if cls is None or cls == class_obj or cls == class_name:
                # Query objects from the session for the current class
                objs = self.__session.query(class_obj).all()
                # Populate the objects dictionary
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objects[key] = obj

        return objects

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session()
