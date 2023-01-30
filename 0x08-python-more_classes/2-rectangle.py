#!/usr/bin/python3
"""Class that defines area and perimeter
"""


class Rectangle:
    """Class defined by width and height.
    Args:
        height (int): height of rectangle
    Attributes:
        width (int): width of rectangle
    """

    def __init__(self, width=0, height=0):
        # attribute that engages the setters defined below
        self.height = height
        self.width = width

    @property
    def height(self):
        """height getter, setter with same method name
        Returns:
            height (int): height of rectangle
        """
        return self.height

    @height.setter
    def height(self, value):
        """Args:
            value (int): height of rectangle
        Attributes:
            __height (int): height of rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """width getter, setter with same method name
        Returns:
            width (int): width of rectangle
        """
        return self.width

    @width.setter
    def width(self, value):
        """Args:
            value (int): width of rectangle
        Attributes:
            __width (int): width of rectangle
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        """Calulates area of rectangle.
        Attributes:
            __height (int): height of rectangle
            __width (int): width of rectangle
        Returns:
            area (int): height times width
        """
        area = self.__height * self.__width
        return area

    def perimeter(self):
         """Calulates perimeter of rectangle.
        Attributes:
            __height (int): height of rectangle
            __width (int): width of rectangle
        Returns:
            perimeter (int): adding all sides
        """
        if width = 0 or height = 0:
            perimeter = 0
        perimeter = 2*self.__height + 2*self.__width
        return perimeter
