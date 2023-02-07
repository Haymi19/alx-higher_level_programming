#!/usr/bin/python3
""" Function that returns True/False if obj is a type of a_class """


def is_same_class(obj, a_class):
    """ Retyrns True if the object is an instance """
    return True if type(obj) == a_class else False
