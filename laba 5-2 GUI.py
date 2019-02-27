#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os

__author__ = "Sergey_Matusevich"


# The program searches for files in the specified directory.
# If the directory is not specified, the search is performed on
# D: er, and the size of the required files is set to 0. That is, all files.

def walk(dir_name="D:\\", min_size=100):
    for address, dirs, files in os.walk(dir_name):
        for file in files:
            addr = address + '/' + file
            if os.path.getsize(addr) >= min_size:
                yield addr


def inserter(value):
    """ Inserts specified value into text widget """
    output.delete("0.0", "end")
    output.insert("0.0", value)


def interceptor():
    try:
        a_val = str(a.get()) or "D:\\"
        b_val = int(b.get() or 0)
        inserter("\n".join(walk(dir_name=a_val, min_size=b_val)))
    except ValueError:
        inserter("""Fill in the correct search parameters. In the field "Specify the size:" enter the number""")


root = Tk()
root.title("Search files by size")
root.minsize(600, 600)
root.resizable(width=False, height=False)

frame = Frame(root)
frame.grid()


def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")



a = Entry(frame, width=3)
a.grid(row=1, column=1, padx=(10, 0), sticky=W + E)
a.bind("<FocusIn>", clear)
a_lab = Label(frame, text="Specify a folder:").grid(row=1, sticky=W)

b = Entry(frame, width=3)
b.grid(row=1, column=4, padx=(10, 0), sticky=W + E)
b.bind("<FocusIn>", clear)
b_lab = Label(frame, text="Specify the size:").grid(row=1, column=3, sticky=W)

output = Text(frame, bg="lightblue", font="Arial 12", width=70, height=30)
output.grid(row=2, columnspan=8)

but = Button(frame, text="Search", command=interceptor).grid(row=1, column=7, padx=(10, 0))

root.mainloop()
