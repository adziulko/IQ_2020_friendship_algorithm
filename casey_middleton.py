import sys

## Function to play friendship algorithm game  
def play_game():
    ## START GAME

    # initialize the user input to 0
    user_entry = 0
    # ask the user to make their own input (1 to play or 2 to exit):
    while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
    # if the user selects 1, they want to play! Ask them questions and wait for their answers.
    while user_entry == 1:
	## STEP 1 HERE
        total_points = 0
        answer_one = int(input('Do you like dogs?\n1. Yes\n2. No\nYour answer: '))
        answer_two = int(input('Do you like to cook?\n1. Yes\n2. No\nYour anser: '))
        answer_three = int(input('DO you like rock climbing?\n1. Yes\n2. No\nYour answer: '))
        answer_four = int(input('Do you like to dance?\n1. Yes\n2. No\nYour answer: '))
        answer_five = int(input('Which is the best Disney princess?\n1. Mulan\n2. Belle\n3.Elsa\n4.Snow White\n5. Rapunzel\nYour answer: '))
        ## STEP 2&3 HERE
        #Q1
        if answer_one == 1: total_points += 5
        else: total_points -= 5
        #Q2
        if answer_two == 1: total_points += 5
        else: total_points -= 5
        #Q3
        if answer_three == 1: total_points += 5
        else: total_points -= 5
        #Q4
        if answer_four == 1: total_points += 5
        else: total_points -= 5
        #Q4
        if answer_five == 1: total_points += 3
        elif answer_five == 2: total_points += 7
        elif answer_five == 3: total_points += 0
        elif answer_five == 4: total_points -= 5
        else: total_points += 2
        ## STEP 4 HERE
        print('You received % out of 32 points!',total_points)
        if total_points >= 25: print("Perfect score! Heyyyyy bestie :)")
        elif total_points > 18: print("We can be really good friends, for sure.")
        elif total_points > 10: print("Sure, we can hang.")
        else: print("Frenemies?")

user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
user_entry = int(user_entry)
	


	
## Function call to play friendship algorithm game
play_game()
