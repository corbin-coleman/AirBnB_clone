#!/usr/bin/python3
"""
City Module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ initializes parent class """
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
