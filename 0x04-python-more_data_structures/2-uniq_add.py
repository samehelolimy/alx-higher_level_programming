#!/usr/bin/python3
# 2-uniq_add.py
# Brennan D Baraban <375@holbertonschool.com>


def uniq_add(my_list=[]):

    result = 0
    for x in set(my_list):
        result += x
    return (result)
