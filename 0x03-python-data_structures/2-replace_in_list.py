#!/usr/bin/python3
# 2-replace_in_list.py
# Brennan D Baraban <375@holbertonschool.com>


def replace_in_list(my_list, idx, element):

    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
