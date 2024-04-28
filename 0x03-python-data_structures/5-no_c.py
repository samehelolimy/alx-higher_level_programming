#!/usr/bin/python3
# 5-no_c.py
# Brennan D Baraban <375@holbertonschool.com>


def no_c(my_string):

    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
