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


		## STEP 1 Question 1	
                total_points = 0
		answer_one = int(input('Are you a morning or night person?\n1. Morning\n2. Night\nYour Answer:'))    


		## STEP 2&3 Question 2
		if answer_one == 1: total_points += 5
		if answer_one == 2: total_points += 4 
		
		 ## STEP 1 Question 2
                answer_two = int(input('Have you seen the show Schitt's Creek?\n1. Yes\n2. No\nYour Answer:'))

                ## STEP 2&3 Question 2
                if answer_two == 1: total_points += 5
                if answer_two == 2: total_points += 2		

		## STEP 1 Question 3
                answer_three = int(input('Do you think it's funny?(Type 1 if you haven't seen it)\n1. Yes\n2. No\nYour Answer:'))

                ## STEP 2&3 Question 3
                if answer_three == 1: total_points += 5
                if answer_three == 2: total_points += 0

		## ## STEP 1 Question 4
                answer_four = int(input('Do you like doing any of these thigns? Mark all that apply:\n1. Rock climbing\n2. Mountain biking\n3. Skiing\n4. Baking and eating sourdough bread\n5. Putting on face masks that make you skin clean and soft (not coronavirus masks)'))

                ## STEP 2&3 Question 4
                if answer_four == 1: total_points += 10
                elif answer_four == 2: total_points += 5
		elif answer_four == 3: total_points += 10
		elif answer_four == 4: total_points += 100
		elif answer_four == 5: total_points += 10

		## STEP 4 HERE
		print(total_points)
		if total_points<=10: print("Sorry. It'll be great working with you but no need to hang out otherwise.")
			elif: total_points>10: print("Let's hang out!")
			else: print("Seems like no points registered for you. That's not a good sign.")
		

		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)
	

	
## Function call to play friendship algorithm game
play_game()
