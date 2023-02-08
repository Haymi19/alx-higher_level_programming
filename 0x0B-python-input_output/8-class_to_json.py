#!/usr/bin/python3
"""
Returns the dictionary description with simple data structure for
a JSON serialization of an object.
"""


def class_to_json(obj):
    """ Return the dictionary description of an object """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
