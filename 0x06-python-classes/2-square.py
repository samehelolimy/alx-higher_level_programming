#!/usr/bin/python3
# 2-square.py
# Brennan D Baraban <375@holbertonschool.com>

class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new Square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
