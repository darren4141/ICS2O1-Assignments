'''
=====================================================================================================================================================================
CIRCLE CALCULATOR PROGRAM VER 2 
DARREN LIU
12/13/2021
PYTHON VER 3.9.1
=====================================================================================================================================================================
PROBLEM DEFINITION: Program to calculate the area, circumference, volume of a sphere, volume of a cylinder, surface area of a sphere, and surface area of a cylinder
INPUT: choice, radius, height
OUTPUT: area/circumference/volume of sphere/volume of cylinder/surface area of a sphere/surface area of a cylinder
PROCESS: various mathematical geometric equations (pi * r^2, etc)
=====================================================================================================================================================================
LIST OF IDENTIFIERS
let pi represent 3.14159
let r represent the radius
let h represent to height
=====================================================================================================================================================================
'''

from ASSIGNMENT_perimeter_area_volume import circumference
'''This function is used to calculate circumference of a circle
    Args:
        r (int or float) = radius
    Returns: int or float: 2*pi*r
'''
from ASSIGNMENT_perimeter_area_volume import area
'''This function is used to calculate the area of a circle
    Args:
        r (int or float) = radius
    Returns: int or float: pi * (r**2)
'''
from ASSIGNMENT_perimeter_area_volume import volume
'''This function is used to calculate the volume of a sphere
    Args:
        r (int or float) = radius
    Returns: int or float: 4/3* (pi **3)
'''
from ASSIGNMENT_perimeter_area_volume import get_radius
'''This function is used to input the radius from the user
    Args:

    Returns:(int) radius inputted
'''
pi = 3.14159
repeat = "y"
def SA_sphere(r):
    '''This function is used to calculate the surface area of a sphere
        Args:
            r (int or float) = radius
        Returns: int or float: 4*pi*(r**2)
    '''
    return 4*pi*(r**2)

def SA_cylinder(r, h):
    '''This function is used to calculate the surface area of a cylinder
        Args:
            r (int or float) = radius
            h (int or float) = height
        Returns: (2 * pi * r *h) + 2*(pi*(r**2))
    '''
    return circumference(r)*h + 2*(area(r))

def VOL_cylinder(r, h):
    '''This function is used to calculate the volume of a cylinder
        Args:
            r (int or float) = radius
            h (int or float) = height
        Returns: (pi*(r**2)) * h
    '''
    return area(r) * h

def get_height():
    '''This function is used to input the height from the user
        Args:

        Returns:(int) height inputted
    '''
    height = int(input("Please enter the height of the cylinder: "))
    return height

def choice():
    '''This function is used to input the choice from the user
        Args:

        Returns:(String) choice entered
    '''    
    ch = input("What would you like to calculate? \n 1) Circumference of a circle \n 2) Area of a circle \n 3) Surface area of a circle \n 4) Volume of a sphere \n 5) Surface area of a cylinder \n 6) Volume of a cylinder \n 7) Exit ")
    return ch

def get_output(ch):
    '''This function is used to take the choice and decides what to calculate
        Args:
            ch(String) = what the user chose to calculate

        Returns:
    '''
    global repeat
    if ch == '1':
        print("Circumference:", "%.5f" % circumference(get_radius()))
    elif ch == '2':
        print("Area of Circle:", "%.5f" % area(get_radius()))
    elif ch == '3':
        print("Surface Area of Sphere:", "%.5f" % SA_sphere(get_radius()))
    elif ch == '4':
        print("Volume of Sphere:", "%.5f" % volume(get_radius()))
    elif ch == '5':
        print("Surface Area of Cylinder:", "%.5f" % SA_cylinder(get_radius(), get_height()))
    elif ch == '6':
        print("Volume of Cylinder:", "%.5f" % VOL_cylinder(get_radius(), get_height()))
    elif ch == '7':
        print("Goodbye")
        repeat = 'n'


def main():
    '''This function is used to loop the choice function until the repeat variable is 'n'
        Args:

        Returns:
    '''
    while repeat != 'n':
        get_output(choice())

main()