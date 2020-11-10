#In this programme i try to simulate the Monty Hall problem.
#This programme is written in python

# 1- search a random number between 1 and 3 which consist to the price
# 2- search a random number which consist to the choice of the player
# 3- search a random number to eliminate one of the other doors
# 4- between the rest of the choices change the chosen number
# 5- check if the chosen number is equal to the number consisted to the price
# 6- make this simulation lots of time

import random

times = 10000
success = 0

for x in range(times):
    price = random.randint(1, 3)
    chosen = random.randint(1, 3)
    # the index of eliminated door should not be the index of the price and it should not be the index of the door chosen
    if price == 1:
        if chosen == 1:
            eliminated = random.randint(2, 3)
        elif chosen == 2:
            eliminated = 3
        else:
            eliminated = 2
    elif price == 2:
        if chosen == 1:
            eliminated = 3
        elif chosen == 2:
            eliminated = random.randint(1, 2)
            if eliminated == 2:   # eliminated is either 1 or 3
                eliminated = 3
        else:
            eliminated = 1
    else:
        if chosen == 1:
            eliminated = 2
        elif chosen == 2:
            eliminated = 1
        else:
            eliminated = random.randint(1, 2)
    #let's change the choice
    if eliminated == 1:
        if chosen == 2:
            chosen = 3
        elif chosen == 3:
            chosen = 2
    if eliminated == 2:
        if chosen == 1:
            chosen = 3
        elif chosen == 3:
            chosen = 1
    if eliminated == 3:
        if chosen == 1:
            chosen = 2
        elif chosen == 2:
            chosen = 1
    #now let's check if the player won
    if price == chosen:
        success += 1

proportion = success/times
percentage = (100 * success)/times
print(percentage)
