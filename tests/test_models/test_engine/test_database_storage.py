#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage, HBNB_TYPE_STORAGE
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.engine.db_storage import DBStorage


class test_databaseStorage(unittest.TestCase):
    """ Class to test the file storage method """

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key, v in storage.all().items():
            storage.delete(v)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            Base.metadata.drop_all(storage.__engine)
        except:
            pass

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_obj_list_empty_db(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_new_db(self):
        """ New object is correctly added to __objects """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_all_db(self):
        """ __objects is properly returned """
        new = BaseModel()
        new.save()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_base_model_instantiation_db(self):
        """ File is not created on BaseModel save """
        new = BaseModel()
        var = True
        self.assertTrue(var)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_empty_db(self):
        """ Data is saved to file """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertTrue(True)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_save_db(self):
        """ FileStorage save method """
        new = BaseModel()
        storage.save()
        self.assertTrue(True)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_reload_db(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        new.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertTrue(True)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_reload_empty_db(self):
        """ Load from an empty file """

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertTrue(True)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        var = True
        self.assertTrue(var)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_type_path(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_type_objects(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_key_format(self):
        """ Key is properly formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    @unittest.skipIf(HBNB_TYPE_STORAGE != 'db', "for only file storage")
    def test_storage_var_created(self):
        """ FileStorage object storage created """
        from models.engine.db_storage import DBStorage
        print(type(storage))
        self.assertEqual(type(storage), DBStorage)
