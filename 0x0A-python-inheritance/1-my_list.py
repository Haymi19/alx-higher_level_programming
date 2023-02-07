#!/usr/bin/python3
""" Classs inherits from another list """


class MyList(list):
    """ Inherits the attributes references of class list """
    def print_sorted(self):
        """ Prints the sorted list in ascending order """
        print(sorted(self))
