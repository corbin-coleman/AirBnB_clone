#!/usr/bin/python3
"""
BaseModel Module
"""
from datetime import datetime
import uuid


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ initializes instance attributes """
        time = '%Y-%m-%d %H:%M:%S.%f'
        dict_found = 0
        for item in args:
            if type(item) is dict:
                dict_found = 1
                self.__dict__ = item
                self.created_at = datetime.strptime(item['created_at'], time)
                if hasattr(item, 'updated_at'):
                    self.updated_at = datetime.strptime
                    (item['updated_at'], time)
        if dict_found == 0:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            from models.__init__ import storage
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

    def to_json(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance + the class name in the key __class__
        """
        newdict = self.__dict__.copy()
        newdict.update({'__class__': self.__class__.__name__})
        if hasattr(self, 'updated_at'):
            newdict.update({'updated_at': str(self.updated_at)})
        newdict.update({'created_at': str(self.created_at)})
        return newdict

    def __str__(self):
        """ prints [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
