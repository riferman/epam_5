#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Sergey_Matusevich"

# Write a wrapper for the os.walk() function that returns a generator
# Make the same function optionally parametrized, let it accept minimal size (in kb) for the files to list


import os


def run_once(func):
    def wrapper(min_size=100):
        for filename in func():
            if os.path.getsize(filename) >= min_size:
                yield filename

    return wrapper


@run_once
def your_wrapper():
    for address, dirs, files in os.walk("C:\\Windows\\Program files"):
        for file in files:
            yield address + '/' + file


# a = walk(min_size=100)
#
# print("размер 100 кб", len(list(a)))  # 100

files_lazy_lister = your_wrapper(min_size=1000)

print("размер 1000 кб", list(files_lazy_lister))  # 1000
