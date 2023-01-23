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

