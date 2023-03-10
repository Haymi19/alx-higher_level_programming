#!/usr/bin/python3
""" subclass MyInt """


class MyInt(int):
    """ Class declaration """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
