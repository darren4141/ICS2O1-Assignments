'''
=====================================================================================================================================================================
DICE ROLLING PROGRAM
DARREN LIU
12/1/2021
PYTHON VER 3.9.1
=====================================================================================================================================================================
Program to generate a given number of dice rolls and tell the user which result was the most frequent and how many times it was rolled
INPUT: number of dice rolls, repeat option
OUTPUT: dice rolls, most frequent number, amount of times the most frequent number showed up
=====================================================================================================================================================================
'''
from random import randrange    #import randrange function 

print("DICE ROLLING PROGRAM")
repeat = "y"    #initialize variable
highest = ""    #initialize variable
highestnum = 0  #initialize variable
while repeat != "n":        #loop for repeat option
    iterations = input("How many times do you want to roll the dice? ")     #input # of dice rolls
    try: #error checking
        times = int(iterations)     #assign iterations input as an int for error checking (input is not a word, or a decimal) and for loop range
        if times < 0:               #condition to check if input is negative
            int("ForceValueError")  #force ValueError if input is negative
        one = two = three = four = five = six = seven = eight = nine = ten = eleven = twelve = 0    #initialize counter variables as zero (done inside the loop so that they reset on repeat)
        for x in range (0, times):  #loop for # of dice rolls
            roll1 = randrange(1, 7) #generate first random die roll
            roll2 = randrange(1, 7) #generate second random die roll
            rollsum = roll1 + roll2 #add first and second dice rolls 

            if rollsum == 2:        #lines 25 - 46: selection to count how many times each number is rolled
                two += 1;
            elif rollsum == 3:
                three += 1;
            elif rollsum == 4:
                four += 1;
            elif rollsum == 5:
                five += 1;
            elif rollsum == 6:
                six += 1;
            elif rollsum == 7:
                seven += 1;
            elif rollsum == 8:
                eight += 1;
            elif rollsum == 9:
                nine += 1;
            elif rollsum == 10:
                ten += 1;
            elif rollsum == 11:
                eleven += 1;
            elif rollsum == 12:
                twelve += 1;
            print(rollsum)          #print dice roll

        if two > three:             #lines 49 - 82: sorting to find the number with the highest frequency, also assigning a new variable to print the actual dice roll number
            highest = two
            frequent = 2
        else:
            highest = three
            frequent = 3

        if highest < four:
            highest = four
            frequent = 4
        if highest < five:
            highest = five
            frequent = 5
        if highest < six:
            highest = six
            frequent = 6
        if highest < seven:
            highest = seven
            frequent = 7
        if highest < eight:
            highest = eight
            frequent = 8
        if highest < nine:
            highest = nine
            frequent = 9
        if highest < ten:
            highest = ten
            frequent = 10
        if highest < eleven:
            highest = eleven
            frequent = 11
        if highest < twelve:
            highest = twelve
            frequent = 12
        
        print("The most frequent roll was", frequent, "which appeared", highest, "times")
        repeat = input("Would you like to repeat the program? (y/n) ") #input repeat decision
    except ValueError:              #error checking for if the # of dice rolls is a number
        print("Make sure your input is a positive integer and try again");