'''
Print the area of a circle, given the radius
'''
import math


def print_area_of_circle(radius):
    area = math.pi * radius * radius
    print(f'The area of a circle is {area:.3f}')


print_area_of_circle(12.4)
