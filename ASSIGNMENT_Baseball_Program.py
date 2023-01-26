'''
=====================================================================================================================================================================
BASEBALL PROGRAM
DARREN LIU
11/4/2021
PYTHON VER 3.6.2
=====================================================================================================================================================================
Program to determine what to do with a baseball batter/pitcher given their average, and keeps track of the number of batters/pitchers released, and sent to each team
INPUT: batter name, batter average, pitcher name, pitcher average
OUTPUT: player contract status per player, overall statistics at the end
=====================================================================================================================================================================
'''

start_choice = "";                                  #initialize repeat variable

while start_choice.casefold() != "d":               #check if user wants to repeat (with capitalization error checking)
    TORbatters = DUNbatters = RELbatters = TORpitchers = DUNpitchers = RELpitchers = 0;                     #initialize all counters as 0
    player = "";                                    #declare and initialize player name
    print("Hello! Welcome to BASEBALL CONTRACT EVALUATOR");
    print("What would you like to do?");
    print("a) enter data for batters");
    print("b) enter data for pitchers");
    print("c) enter data for batters and pitchers");
    print("d) exit");
    start_choice=input();                           #INPUT: user choice
    
    if start_choice.casefold() != "d":              #SELECTION: user choice cannot be "d"
        
        while player.casefold() != "stop" and start_choice.casefold() != "b":                                   #LOOP: end condition is the player name being "stop" or if user choice is "b"
            player=input("Please enter your name, batter. Enter 'stop' once all batters have been entered ");   #INPUT: batter name

            if player.casefold() != "stop":         #SELECTION: player name cannot be stop
                average=input("Please enter your batting average "); #INPUT: batting average
                try:                                #error checking
                    val = float(average);           #error check: turn average into a number
                    if val >= 300:                  #SELECTION: see if average is good enough for toronto
                        print(player, "you are good enough to be sent to Toronto");
                        TORbatters += 1;            #PROCESS: add to counter
                    elif val >= 275:                #SELECTION: see if average is good enough for dunedin
                        print(player, "you are good enough to be sent to Dunedin");
                        DUNbatters += 1;            #PROCESS: add to counter
                    elif val < 275:                 #SELECTION: release player if their average is too low for dunedin
                        print(player, "you have been released");
                        RELbatters += 1;            #PROCESS: add to counter
                        
                except ValueError:                  #if the average is not a number
                    print("Please enter a number, try again");

        player = ""                                 #change player name so it isn't "stop"

        while player.casefold() != "stop" and start_choice.casefold() != "a":                                   #LOOP: end condition is the player name being "stop" or if user choice is "a"
            player=input("Please enter your name, pitcher. Enter 'stop' once all pitcher have been entered ");  #INPUT: pitcher name
            
            if player.casefold() != "stop":         #SELECTION: if player name is stop don't ask them for their average
                average=input("Please enter your average pitch speed "); #INPUT: pitch average
                try:                                #error checking
                    val = float(average);           #error check: turn average into a number
                    if val > 87:                    #SELECTION: to see if average is good enough for toronto
                        print(player, "you are good enough to be sent to Toronto");
                        TORpitchers += 1;           #PROCESS: add to counter
                    elif val > 82:                  #SELECTION: see if average is good enough for dunedin
                        print(player, "you are good enough to be sent to Dunedin");
                        DUNpitchers += 1;           #PROCESS: add to counter
                    elif val <= 82:                 #SELECTION: release player if their average isn't good enough for dunedin
                        print(player, "you have been released");
                        RELpitchers += 1;           #PROCESS: add to counter
                        
                except ValueError:                  #if the average is not a number
                    print("Please enter a number, try again");

    if start_choice.casefold() != "d":                                  #SELECTION: if the initial choice is not "d) exit"
        print("DATA:");
        print("Toronto players:", TORbatters + TORpitchers);            #output total toronto players
        print("  ", TORbatters, "batters");                             #output number of toronto batters
        print("  ", TORpitchers, "pitchers");                           #output number of toronto pitchers
        print();
        print("Dunedin players:", DUNbatters + DUNpitchers);            #output total dunedin players
        print("  ", DUNbatters, "batters");                             #output total dunedin batters 
        print("  ", DUNpitchers, "pitchers");                           #output total dunedin pitchers 
        print();
        print("Released players:", RELbatters + RELpitchers);           #output total released players
        print("  ", RELbatters, "batters");                             #output total released batters
        print("  ", RELpitchers, "pitchers");                           #output total released pitchers

print("Thanks you for using the BASEBALL CONTRACT EVALUATOR!");