#!/usr/bin/python3
# 100-safe_print_integer_err.py
# Brennan D Baraban <375@holbertonschool.com>

import sys


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
