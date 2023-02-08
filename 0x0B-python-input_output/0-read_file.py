#!/usr/bin/python3
""" Function which reads from a file and prints it in stdout """


def read_file(filename=""):
    """
    Function that reads from a file

    Args:
        filename: filename
    """

    with open(filename, "r", encoding="utf-8") as t:
        read_data = t.read()
        print(read_data, end="")
