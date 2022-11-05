#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_tup = ()
    for i in range(2):
        a = 0 if i >= len_a else tuple_a[i]
        b = 0 if i >= len_b else tuple_b[i]
        new_tup = (a + b) if (i == 0) else (new_tup, a + b)
    return (new_tup)
