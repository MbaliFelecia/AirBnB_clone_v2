#!/usr/bin/python3
"""If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
instantiates a database storage engine (DBStorage).
Otherwise, instantiates a file storage engine (FileStorage)"""
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

type_storage = os.getenv('HBNB_TYPE_STORAGE')

if type_storage == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
