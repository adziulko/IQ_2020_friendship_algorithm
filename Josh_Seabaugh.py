import sys
  
## Function to play friendship algorithm game
def play_game():
        ## START GAME

        # initialize the user input to 0
	user_entry = 0
        # ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
        # if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
                ## STEP 1 HERE
		total_points = 0
		q1 = int(input('Do you like sports?\n1. Yes\n2. No\n\nYour Selection: '))

		if q1 == 2:
			total_points -= 5
		elif q1 == 1:
			total_points += 5
			q1_b = int(input("\nDo you like basketball?\n1. Yes\n2. No\n\nYour Selection: "))
			if q1_b == 1:
				total_points += 10
			elif q1_b == 2:
				total_points -= 5
		else:
			sys.exit("Not a valid answer, try again.")
                ## STEP 2&3 HERE
		q2 = int(input('Do you like the great outdoors?\n1. Yes\n2. No\n\nYour Selection: '))

		if q2 == 1:
			total_points += 5
		elif q2 == 2:
			total_points -= 5
		else:
			sys.exit("Not a valid answer, try again.")

		q3 = int(input('Do you like dogs?\n1. Yes\n2. No\n\nYour Selection: '))

		if q3 == 1:
			total_points += 5
		elif q3 == 2:
			total_points -= 5
		else:
			sys.exit("Not a valid answer, try again.")

		q4  = int(input('Can you provide me with food?\n1. Yes\n2. No\n\nYour Selection: '))

		if q4 == 1:
			total_points += 20
		elif q4 == 2:
			total_points -= 5
		else:
			sys.exit("Not a valid answer, try again.")
                ## STEP 4 HERE

		print("\n\nTotal points: " + str(total_points))
		if total_points >= 40: print("Best Friends!")
		elif total_points >= 15 and total_points < 40: print("Friends!")
		elif total_points >= 5 and total_points < 15: print("I guess we can hang out...")
		else: print("Friends? Nope.")

		user_entry = test_int(input('\nSelect Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))

## Function call to play friendship algorithm game
play_game()

