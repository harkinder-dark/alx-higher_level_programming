#!/usr/bin/python3

"""
    rectangle classs
"""


class Rectangle:
    """
        rectangle class define
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
            initialisation
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
            height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
            area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
            perimetre
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__width + self.__height) * 2

    def __str__(self):
        """
            string => __str__
        """
        if self.__height == 0 or self.__width == 0:
            return ""

        s = (str(Rectangle.print_symbol) * self.width + "\n") * self.height
        return s[:-1]

    def __repr__(self):
        """
            string => __rpr__
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
            del
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            return rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
