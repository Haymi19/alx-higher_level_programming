#!/usr/bin/python3
""" Class Student that defines a student """


class Student:
    """ class defined by first_name, last_name and age """

    def __init__(self, first_name, last_name, age):
        """ Function that defines a class """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns directory description """

        return self.__dict__.copy()
