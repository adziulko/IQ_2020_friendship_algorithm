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
                answer_one = int(input('Does your mama dance?\n1. Yes\n2. No\nYour Answer:'))
                if answer_one == 1: total_points += 5
                else: total_points += 0
                ## STEP 2&3 HERE
                answer_two = int(input('Does your daddy rock n roll?\n1. Yes\n2. No\nYour Answer:'))
                if answer_two == 1: total_points += 5
                else: total_points += 0
                answer_three = int(input('Do you kick off your Sunday shoes?\n1. Yes\n2. No\nYour Answer:'))
                if answer_three == 1: total_points +=5
                else: total_points += 0

		## STEP 4 HERE
                answer_four =  int(input('Are you in the danger zone?\n1. Yes\n 2. No\nYour Answer:'))
                if answer_four == 1: total_points += 5
                else: total_points += 0
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)
	


	
## Function call to play friendship algorithm game
play_game()
