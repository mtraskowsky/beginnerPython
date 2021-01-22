# Name: Maria Traskowsky
# Section: (C) TU 11:00am - 12:15pm
# Project: Snack Machine
# Description: This project represents a finite state machine that represents a snack machine.
# The snack machine takes in user inputs for amount of money, which snack the user wants, and
# also asks whether the user wants a refund. The program also calculates the change
# that is owed. The program restocks the snack machine to the initial amounts. 
# The states are described in further detail below.

# State A = Start or Idle
# State B = Insert. Will accept an input of coins from user input or can accept refund to cancel the transaction
# State C = Select. Will ask a user to choose a snack. Should take input of all 3 snacks and if the user wants a refund
# State D = State should dispense a snack to the user, saying "Dispensing Snack" and charge the user
# State E = Return change. State should return the amount of change and say "Returning Change" and the amount given back
# EXTRA CREDIT: State F = Stock. This state should restock machine with initial quantity for each item when the machine started.
# State G = Off. This represents when the machine is turned off



# START 

total_inserted = 0

# each snack costs $1.00
snack_1_initial_value = 2
snack_1 = snack_1_initial_value

snack_2_initial_value = 4
snack_2 = snack_2_initial_value

snack_3_initial_value = 1
snack_3 = snack_3_initial_value

state = 'A'

# State A: Start or Idle
while (state == 'A'): 
    print()
    start_program = str(input("If you would like to start the program, type 'START'. If not, type 'IDLE': "))
    if (start_program == 'START'):
        print("Program is starting") 
        state = 'B' 
        break
    elif (start_program == 'IDLE'):
        state =='A'


# State B: Insert - accepts user input for amount of coins    
while (state == 'B'):
    print()
    total_inserted = float(input("Enter the amount of money that you have: "))
    if (total_inserted >= 1.00):
        print("You have enough money for a snack.")
        refund = str(input("Would you like a refund? (YES/NO): "))                
        if (refund == 'YES'):
            state = 'E'
            break
        if (refund == 'NO'):
            state = 'C'
        
    elif (total_inserted < 1.00):
        print("You don't have enough money.")     
        refund = str(input("Would you like a refund? (YES/NO): "))                
        if (refund == 'YES'):
            state = 'E'
            break
        else:
            state = 'B'


# State C: Select - user selects which snack they want
num_snacks = 0
while (state == 'C'):
    print()
    print("Quantity of snack 1: " + str(snack_1) + " available.")
    print("Quantity of snack 2: " + str(snack_2) + " available.")
    print("Quantity of snack 3: " + str(snack_3) + " available.")
    print()

    snack_choice = str(input("What snack would you like? Please type '1', '2', or '3'. If you would like a refund instead, please type 'REFUND': "))
    if (snack_choice == 'REFUND'):
        print("Giving you a refund now.")
        state = 'E'
        break
    if (int(snack_choice) == 1): 
        print("You chose snack 1.")
        snack_1 = snack_1 - 1
        num_snacks += 1
        state = 'D'
    if (int(snack_choice) == 2):
        print("You chose snack 2.")
        snack_2 = snack_2 - 1 
        num_snacks += 1
        state = 'D'
    if (int(snack_choice) == 3): 
        print("You chose snack 3.")
        snack_3 = snack_3 - 1
        num_snacks += 1
        state = 'D'
        

# State D: Dispenses snack to user
while (state == 'D'):
    print()
    print("Dispensing snack " + snack_choice)
    charge_for_snack = 1.00 * num_snacks
    print("Charge for the snack is " + '${:,.2f}'.format(charge_for_snack))
    print()
    state = 'E'


# Returns change to user, displaying "Returning Change" and the amount
while (state == 'E'):
    charge_for_snack = 1.00 * num_snacks

    print()
    amount_of_change = total_inserted - charge_for_snack
    print("Returning change: " + '${:,.2f}'.format(amount_of_change))
    state = 'F'

# EXTRA CREDIT 
while (state == 'F'):
    print()
    print("Restocking machine..")
    snack_1 = snack_1_initial_value
    print("Quantity of snack 1: " + str(snack_1) + " available.")

    snack_2 = snack_2_initial_value
    print("Quantity of snack 2: " + str(snack_2) + " available.")

    snack_3 = snack_3_initial_value
    print("Quantity of snack 3: " + str(snack_3) + " available.")

    print()
    state = 'G'

# Machine is off
while (state == 'G'):
    state = 'A'
    


