import sys

def test_int(x):
	try:
		y = int(x)
	except Exception as e:
		raise ValueError("Answer must be an integer!")
	return(y)

## Function to play friendship algorithm game
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
	while (user_entry != 1 and user_entry != 2):
		user_entry = test_int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
		## STEP 1 HERE
		total_points = 0
		q1 = test_int(input("\nDo you enjoy reading books?\n1: Yes\n2: No\n\nYour Selection: "))

		## STEP 2&3 HERE
		if q1 == 1:
			total_points += 10
		elif q1 == 2:
			total_points -= 5
		else:
			sys.exit("Not a valid answer, try again.")

		q2 = test_int(input("\nDo you prefer banana bread with chocolate chips or without?\n"
					"1: With chocolate!\n2: Without chocolate\n3: Don't care\n4: I don't like banana bread\n\n"
					"Your Selection: "))
		if q2 == 2:
			total_points -= 10
		elif q2 == 3:
			total_points += 5
		elif q2 == 4:
			total_points -= 5
		elif q2 == 1:
			total_points += 10
			q2_b = test_int(input("\nWhat kind of chocolate do you prefer?\n"
						"1: White chocolate\n2: Milk chocolate\n3: Dark chocolate\n\n"
						"Your Selection: "))
			if q2_b == 1:
				total_points -= 10
			elif q2_b == 2:
				total_points += 0
			elif q2_b == 3:
				total_points += 10
		else:
			sys.exit("Not a valid answer, try again.")

		q3 = test_int(input("\nFill in the blank: You are an ____vert.\n"
							"1: Intro\n2: Extra\n3: Ambi\n\nYour Selection: "))
		if q3 == 2:
			total_points -= 5
		elif q3 == 3:
			total_points += 5
		elif q3 == 1:
			total_points += 0
		else:
			sys.exit("not a valid number, try again.")

		q4 = input("\nDo you enjoy any of the following foods? (type all numbers that apply)\n"
					"1: cheese\n2: cream cheese\n3: jelly\n4: peanut butter\n5: olives\n6: don't like any of these\n\n"
					"Your Selection: ")
		if "2" in q4:
			total_points -= 5
		if "3" in q4:
			total_points += 0
		if "4" in q4:
			total_points += 0
		if "1" in q4:
			q4_b = test_int(input("\nDo you force your love of cheese on others?\n"
						"1: Yes\n2: No\n\n"
						"Your Selection: "))
			if q4_b == 1:
				total_points -= 10
			elif q4_b == 2:
				total_points += 5
		if "5" in q4:
			q4_c = test_int(input("\nWhat kind of olives do you like?\n"
						"1: Green\n2: Black\n\n"
						"Your Selection: "))
			if q4_c == 1:
				total_points -= 0
			elif q4_c == 2:
				total_points += 5
		else:
			sys.exit("Not a valid answer, try again.")
		## STEP 4 HERE
		print("\n\nTotal points: " + str(total_points))
		if total_points > 10: print("We'd be good friends!")
		elif total_points > -15: print("We'd be friendly acquaintances.")
		elif total_points > -30: print("We'd be distant acquaintances...")
		else: print("Hmm... Probably not super compatible personalities but you do you.")

		user_entry = test_int(input('\nSelect Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))

## Function call to play friendship algorithm game
play_game()
