#!/usr/bin/python3


def no_c(my_string):
    """
    removes all characters 'c' and 'C' from s
    """
    return "".join(i for i in my_string if i not in "cC")
