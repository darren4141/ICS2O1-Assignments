#Rectangle/triangle generator
#Assignment - Rectangle and Triangle
#Darren Liu

print("HOLLOW RECTANGLE OR TRIANGLE GENERATOR");
#inputs length + width or inputs base
#inputs symbol
#constructs shape with given dimensions and symbol
repeat = "y";   #initialize repeat variable as yes

while repeat.casefold() == "y":    #loop entire program to give user a choice to repeat
    print("what shape would you like me to make?"); #let user decide on shape
    print("a) rectangle");
    print("b) triangle");
    choice=input();

    if choice.casefold() == "a":   #if statement for rectangle
        length=int(input("please enter the length of your rectangle: "));   #input length as an integer
        width=int(input("please enter the width of your rectangle: ")); #input width as an integer
        s=input("what material do you want the rectangle to be made out of (1 character only)? ");   #input symbol as char
        for i in range (1, length + 1):     #for loop to construct rectangle length
            for j in range(1, width + 1):   #nested for loop to construct width
                    if i == 1 or i == length or j == 1 or j == width:   #condition to print rectangle borders
                        print(s, end=" ")
                    else:   #condition to make the rectangle hollow
                        print(" ", end=" ")
            print() #start printing on the next line


    elif choice.casefold() == "b":   #if statement for triangle
        t=int(input("please enter the base of your triangle: "));   #input base/height as an integer
        s=input("what material do you want the triangle to be made out of (1 character only)? ");    #input symbol as char
        t+= 1
        for i in range (1, t):  #for loop to construct triangle base
            for j in range(1, i+1): #nested for loop to construct triangle diagonal
                    if i == 1 or i == t-1 or j == 1 or j == i:  #condition to print triangle borders
                        print(s, end=" ")
                    else:   #condition to make the triangle hollow
                        print(" ", end=" ")
            print() #start printing on the next line
    else:   #if user doesn't enter a or b it prompts them to enter a valid answer and restarts the program
        print("please enter a valid answer: 'a' or 'b'");
        
    if choice.casefold() == "a" or choice.casefold() == "b":  #if choice is invalid prompt to repeat is not needed
        repeat = input("would you like to repeat the program? (y/n) "); #input repeat choice as a char
        
print("program ending");