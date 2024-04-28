#!/usr/bin/python3
# 0-safe_print_list.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_list(my_list=[], x=0):
    """Print x elements of alist"""
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
