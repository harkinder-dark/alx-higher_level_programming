#!/usr/bin/python3
"""function for file read
"""


def read_file(filename=""):
    """filename: name of file
        print file contains in the stdout
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        file.read()
