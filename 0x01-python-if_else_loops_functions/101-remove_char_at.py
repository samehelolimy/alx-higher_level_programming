#!/usr/bin/python3
# 101-remove_char_at.py
# Brennan D Baraban <375@holbertonschool.com>


def remove_char_at(str, n):

    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
