"""
Task:
In this problem, you are to find a point’s location with respect to the unit circle and the angle it makes with the x-axis.
Location can be on/in/outside the circle. For angle (θ) calculation, you need to use arctan (from the math library) to find in terms of radian 
and convert it to degree.
Definition: A unit circle is a circle on the Cartesian Plane that has a radius of 1 unit and is centered at the origin
(0, 0).
"""

import math


def calculate_angle(coordinates):
    """
    This function takes the coordinates of a point as a tuple and
    calculates the angle (in terms of degree) and return it.

    :param coordinates (tuple): coordinates[0]: the value an apsis
                                 coordinates[1]: the value an ordinate

    :return: the positive angle (in terms of degree) that is between apsis
             and the ray drawn from center to the point
    """
    try:
        angle_radian = math.atan(coordinates[1]/coordinates[0])
        angle_degree = math.degrees(angle_radian)
        if angle_degree <= 0:
            if coordinates[0] < 0:      # checking region between 90.0 and 180.0
                angle_degree = 180.0 + angle_degree
                return angle_degree
            else:                      # checking region between 270.0 and 360.0
                if angle_degree == 0.0:
                    return angle_degree
                else:
                    angle_degree = 360.0 + angle_degree
                    return angle_degree
        else:
            if coordinates[1] < 0:    # checking region between 180.0 and 270.0
                angle_degree = 180 + angle_degree
                return angle_degree
            else:                     # checking region between 0.0 and 90.0
                return angle_degree

    except ZeroDivisionError:
        if coordinates[1] > 0:
            return 90.0
        else:
            return 270.0


def check_point_loc(coordinates):
    """
    This function find the location of the point and prints its location
    e.g. prints "outside the unit circle" if it is outside the unit circle
    or prints "on the unit circle" if it is on the unit circle
    or prints "in the unit circle" if it is in the unit circle.

    :param coordinates (tuple): coordinates[0]: the value on apsis
                                coordinates[1]: the value on ordinate
    """
    distance = (coordinates[0] ** 2) + (coordinates[1] ** 2)
    if distance == 1:
        print("on the unit circle")
    elif distance > 1:
        print("outside the unit circle")
    else:
        print("in the unit circle")


if __name__ == '__main__':
    coordinates = tuple(map(float, input().split()))
    check_point_loc(coordinates)
    print(calculate_angle(coordinates))
