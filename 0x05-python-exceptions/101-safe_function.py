#!/usr/bin/python3


def safe_function(fct, *args):
    """
    executes a function safely and return the result of the function
    """
    try:
        return fct(*args)
    except Exception as e:
        import sys
        print(f"Exception: {e}", file=sys.stderr)
        return None
