# Name: Maria Traskowsky
# Section: (C) TU 11:00am - 12:15pm
# Project: Pickup Sticks Game
# Description: This project creates a 2 player game, called Sticks.
# The game starts with 20 sticks, and each player can just 1-3 sticks during their turn.
# The player who takes the last stick loses. 
# The number of sticks are displayed, and will reflect the amount of sticks left as the players remove sticks. 

# start with 20 sticks
num_sticks = 20
print_sticks = 'Y'
# start with the first player
player_turn = 1
# this while loop will print out the number of sticks during the game, starting with 20
while (print_sticks == 'Y' and num_sticks >= 0):
    for row in range(1, 6):
        if (num_sticks > 9):
            print("| " * 9 + "|  " * (num_sticks - 9))
        if (num_sticks < 10):
            print("| " * num_sticks)
        print("")
    for i in range(num_sticks):
        print((i + 1), end = ' ')
    print("")
    print_sticks = 'S'

    # player A's turn
    if (player_turn == 1):
        print("")
        # when there are only two sticks left, the player can only take 1 or 2 sticks
        if (num_sticks == 2):
            print("There are only 2 sticks left, so only choose to take 1 or 2 on this turn.")
        # when there is only one stick left, the player has to take it
        if (num_sticks == 1):
            print("There is only 1 stick left, so you have to take the last one.")
        # ask player how many sticks they want to take
        less_sticks = int(input("Player A, how many sticks do you want to remove? (1-3): "))
        # if the player chooses too many or too few sticks, prompt them to try again
        while (less_sticks < 1 or less_sticks > 3):
            less_sticks = int(input("You can only choose 1, 2, or 3 sticks per turn. Please try again: "))
        num_sticks = num_sticks - less_sticks
        # player loses when they take the last remaining stick
        if (num_sticks == 0):
            print("Player A took the last stick. Player A lost!")
            continue
        # prints out how many sticks the player picked up, as well as how many sticks are left
        print("Player A took " + str(less_sticks) + " stick(s). There are " + str(num_sticks) + " stick(s) left.")
        print("")
        # print out number of sticks
        print_sticks = 'Y'
        # switch to player B
        player_turn = 2
        continue

    # player B's turn
    if (player_turn == 2):  
        print("")  
        # when there are only two sticks left, the player can only take 1 or 2 sticks
        if (num_sticks == 2):
            print("There are only 2 sticks left, so only choose to take 1 or 2 on this turn.")
        # when there is only one stick left, the player has to take it
        if (num_sticks == 1):
            print("There is only 1 stick left, so you have to take the last one.")
        # ask player how many sticks they want to take
        less_sticks = int(input("Player B, how many sticks do you want to remove?: "))
        # if the player chooses too many or too few sticks, prompt them to try again
        while (less_sticks < 1 or less_sticks > 3):
            less_sticks = int(input("You can only choose 1, 2, or 3 sticks per turn. Please try again: "))        
        num_sticks = num_sticks - less_sticks
        # player loses when they take the last remaining stick
        if (num_sticks == 0):
            print("Player B took the last stick. Player B lost!")
            continue
        # prints out how many sticks the player picked up, as well as how many sticks are left
        print("Player B took " + str(less_sticks) + " stick(s). There are " + str(num_sticks) + " stick(s) left.")
        print("")
        # print out number of sticks
        print_sticks = 'Y'
        # switch to player A
        player_turn = 1
        continue


