#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(f"{value} is not an integer")

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(f"{value} is not an integer")

value = "Holberton"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print(f"{value} is not an integer")
