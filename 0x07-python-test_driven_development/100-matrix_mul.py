#!/usr/bin/python3

"""
    matrix function complete
"""


def matrix_mul(m_a, m_b):
    """
        m_a: array of integer or float
    """
    
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")

        if i is None:
            raise ValueError("m_a can't be empty")

        size = len(m_a[0])
        
        for j in i:
            if j is None:
                raise ValueError("m_a can't be empty")

            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")

        if len(i) != size:
            raise TypeError("each row of m_a must be of the same size")


    for j in m_b:
        if type(j) is not list:
            raise TypeError("m_b must be a list of lists")

        if j is None:
            raise ValueError("m_b can't be empty")

        size = len(m_b[0])
        
        for k in j:
            if k is None:
                raise ValueError("m_b can't be empty")

            if type(k) is not int and type(k) is not float:
                raise TypeError("m_b should contain only integers or floats")

        if len(j) != size:
            raise TypeError("each row of m_b must be of the same size")


    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = []
    for i in range(len(m_a)):
        line = []
        for j in range(len(m_b[0])):
            n = 0
            for k in range(len(m_a[0])):
                n += m_a[i][k] * m_b[k][j]
            line.append(n)
        matrix.append(line)

    return matrix