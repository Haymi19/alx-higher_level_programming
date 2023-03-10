#!/usr/bin/python3
"""
Executes a function that inserts a line
of text to a file, after each line containing a specific
string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append a new line when a string is found

    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as t:
        for line in t:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as t:
        t.write("".join(res_line))
