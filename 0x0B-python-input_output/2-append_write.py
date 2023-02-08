#!/usr/bin/python3
""" Function that appends a string at the end of a text file and 
returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends to a text file.

    Args:
        filename: filename
        text: text to write
    """

    with open(filename, "a", encoding="utf-8") as t:
        return t.write(text)
