#!/usr/bin/python3
""" BaseGeometry """


class BaseGeometry:
    """ Empty class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a value as an integer

        Args:
            name(str): The name of the parameter.
            value(int): The parameter to be validated

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
