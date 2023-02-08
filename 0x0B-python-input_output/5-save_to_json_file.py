#!/usr/bin/python3
""" Write an object to a text file using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file by a JSON representation

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: when the object can't be serialized
    """

    with open(filename, 'w', encoding="utf-8") as t:
        json.dump(my_obj, t)
