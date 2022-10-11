#!/usr/bin/python3
"""tache 2 description d'une class vide"""


class Square:
    """ definition de la fonction init de square"""
    def __init__(self, size=0):
        """init function"""
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """the square area"""
        return self.__size ** 2
