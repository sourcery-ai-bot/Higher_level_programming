#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    return (a + b) if c > b else (a * b - c)
