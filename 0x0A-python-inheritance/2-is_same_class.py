#!/usr/bin/python3
"""verify is class instance
"""


def is_same_class(obj, a_class):
    """obj: object  verifying
        a_class: class
        return boolean
    """
    if type(obj) == a_class:
        return True

    return False
