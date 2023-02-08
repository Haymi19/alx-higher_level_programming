#!/usr/bin/python3
""" Returns the JSON representation of an object """

import json


def to_json_string(my_obj):
    """
    Return JSON representation of an object.

    Args:
        my_obj: object

    Raises:
        Exception: if the object can be serialized.
    """

    return json.dumps(my_obj)
