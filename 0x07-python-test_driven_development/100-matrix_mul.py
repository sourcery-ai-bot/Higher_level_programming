#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:43:34 2020

@author: Robinson Montes
"""


def check_matrix(matrix, name):
    """
    Check if list of list is a matrix of integer/float

    Args:
        matrix (list of list): list of list of int or float
        name (str): matrix name to test

    Raises:
        TypeError: Exception if elements in matrix and div are not integer or
            float; Each row in the matrix have the same size

    Return:
        matrix if input is a matrix

    """
    if type(matrix) is not list:
        raise TypeError(f"{name} must be a list")
    if len(matrix) == 0:
        raise ValueError(name + " can't be empty")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(f"{name} must be a list of lists")
        if len(row) == 0:
            raise ValueError(name + " can't be empty")
        for ele in row:
            if type(ele) not in [int, float]:
                raise TypeError(f"{name} should contain only integers or floats")
        if len(row) != len(matrix[0]):
            raise TypeError(f"each row of {name} must be of the same size")


def matrix_mul(m_a, m_b):
    """
    Multiply two matrix

    Args:
        m_a (list): First matrix
        m_b (list): second matrix

    Returns:
        The result of multiply m_a by m_b

    """
    check_matrix(m_a, 'm_a')
    check_matrix(m_b, 'm_b')
    cols_a = len(m_a[0])
    rows_b = len(m_b)

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")
    rows = len(m_a)
    cols = len(m_b[0])
    result = []
    for _ in range(rows):
        fil = [0 for _ in range(cols)]
        result.append(fil)
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
