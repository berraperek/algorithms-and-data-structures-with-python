"""
Give an example of a Python code fragment that attempts to write an element to a list based on an index that may
be out of bounds. If that index is out of bounds, the program should catch the exception that results, and print the
following error message: “Don’t try buffer overflow attacks in Python!”
"""

def out_of_bounds(data, index, element):
    """
    This function writes an element to a list based on
    an index. If that index is out of bounds, the function
    catches the exception.

    """
    try:
        data[index] = element
        return data
    except IndexError:
        print("Don't try buffer overflow attacks in Python!")

