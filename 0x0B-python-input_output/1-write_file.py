#!/usr/bin/python3
""" Function that writes to a file """


def write_file(filename="", text=""):
    """
    Writes to a text file.

    Args:
        filename: filename
        text: text to write
    """

    with open(filename, "w", encoding="utf-8") as t:
        return t.write(text)
