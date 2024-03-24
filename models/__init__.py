#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.base_model import *
from models.city import City
from models.state import State
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity

HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    "use database storage"
    storage = DBStorage()
    """
    create tables in  database and set up session
    database for (quering, adding objs, del objects)
    """
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    "use file storage"
    storage = FileStorage()
    "reload all objects from file"
    storage.reload()
