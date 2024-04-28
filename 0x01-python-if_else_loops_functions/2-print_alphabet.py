#!/usr/bin/python3
# 2-print_alphabet.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print the alphabet in lowercase"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
