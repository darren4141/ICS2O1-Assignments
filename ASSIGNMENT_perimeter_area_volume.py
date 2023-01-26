'''
=====================================================================================================================================================================
CIRCUMFERENCE, AREA, AND VOLUME WHEN GIVEN THE RADIUS PROGRAM
DARREN LIU
12/7/2021
PYTHON VER 3.9.1
=====================================================================================================================================================================
Program to provide the area, circumference, or volume of a circle/sphere when given the radius
INPUT: repeat option, choosing what to calculate (a, b, c), radius
OUTPUT: circumference/area/volume, error messages, restart prompt
=====================================================================================================================================================================
'''

pi = 3.14159    #initalize pi variable
start = 'y'     #initialize start/repeat variable

def choice():#USER SELECTION FUNCTION
    while True: #loop for error checking
        try:    #error checking
            ch = input("What would you like to calculate? \n a)circumference \n b)area \n c)volume ")   #input choice (a, b, c)
            if ch.casefold() != "a" and ch.casefold() != "b" and ch.casefold() != "c":                  #condition for error checking. If choices aren't a, b, c
                int("ForceValueError") #force value error if choice isnt a, b, c
            break;
        except ValueError:  #if there is a value error
            print("Please enter a valid answer (a, b, c)")
    return ch               #return choice

def get_radius():   #INPUT RADIUS FUNCTION
    while True:     #loop for error checking
        try:        #error checking
            radius = input("Please enter the radius of the circle/sphere: ") #input the radius
            radius = float(radius)  #error checking (assign the variable to float)
            if radius < 0:          #condition for error checking. Radius can't be negative
                int("ForceValueError") #force value error if radius is negative
            break;
        except ValueError:          #if there is a value error
            print("Please enter a positive number")
    return radius                   #return the radius
        

def circumference(r): #CIRCUMFERENCE FUNCTION
    circumference = 2 * pi * r      #calculating circumference
    return circumference            #return circumference

def area(r): #AREA FUNCTION
    area = pi * (r**2)              #calculating area
    return area                     #return area

def volume(r): #VOLUME FUNCTION
    volume = (4/3)*pi*(r**3)        #calculating volume
    return volume                   #return volume

def get_output(choice): #OUTPUT FUNCTION
    if choice.casefold() == 'a':                                #if condition for when circumference is chosen
        print("Circumference:", "%.5f" % circumference(get_radius()))#print circumfrence using circumference function and radius (formatted to 5 decimal places)
    elif choice.casefold() == 'b':                              #if condition for when area is chosen
        print("Area:", "%.5f" % area(get_radius()))             #print area using area function and radius (formatted to 5 decimal places)
    elif choice.casefold() == 'c':                              #if condition for when volume is chosen
        print("Volume", "%.5f" % volume(get_radius()))          #print volume using volume function and radius (formatted to 5 decimal places)

while start.casefold() != 'n':                                  #loop with exit condition of start variable being 'n'
    start = input("Would you like to use the CIRCLE CALCULATOR PROGRAM? (y/n) ")#input start/repeat variable
    if start.casefold() == 'y':                                 #condition for if start is 'y'
        get_output(choice())                                    #run 'choice' function and then run 'get_output' function

print("Thanks for using the program!")
