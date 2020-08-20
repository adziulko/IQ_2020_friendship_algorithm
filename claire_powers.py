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
		answer_one = int(input('Are you a morning or night person?\n1. Morning\n2. Night\nYour Answer:'))    

		## STEP 2&3 HERE
		if answer_one == 1: total_points += 5
		if answer_one == 2: total_points += 4 

	
		## STEP 4 HERE
		print(total_points)
		if total_points<=10: print("Sorry. It'll be great working with you but no need to hang out otherwise.")
			elif: total_points>10: print("Let's hang out!")
			else: print("Seems like no points registered for you. That's not a good sign.")
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)
	


	
## Function call to play friendship algorithm game
play_game()
