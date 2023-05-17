#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
<<<<<<< HEAD
    return (int(a) + int(b))
=======
    return (int(a) + int(b))
>>>>>>> 794dfd6001c49175722869db89099f54e4f0452b
