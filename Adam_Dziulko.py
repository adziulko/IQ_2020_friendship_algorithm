import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	user_entry = int(user_entry)
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while int(user_entry) == 1:
		## STEP 1 HERE
		total_points = 0
		answer_one = int(input("Do you want to be BFF's?\n1. Yes\n2. No\n\nYour Selection: "))		
		## STEP 2&3 HERE
		if answer_one == 1:
			input("Congratz! We are now BFF's!\nPress enter to schedule a time to hangout")
		elif answer_one == 2: 
			answer_one_two = int(input("Are you sure?\n1.Yes, Def\n2.Nah, lets be BFF's\n\nYour Selection: "))
			if answer_one_two == 1 :
				input("Your loss") 
			break
		## q2
		answer_two = int(input("Jk, we should get to know each other first. Are you a good person?\n1.Yes\n2.No\n\nYour selection: "))
		if answer_two == 1 : total_points =+ 5
		elif answer_two == 2 : total_points =+ 1
		else: total_points += 0
		## Q3
		answer_three = int(input("If you were a bad person would you actually admit to it or have the self-awareness to judge that?\n1.Yes\n2.No\n\nYour selection: "))
		if answer_three == 1: total_points += 5
		elif answer_three == 2: total_points += 3
		else: total_points += 0
		## Q4
		answer_four = int(input("What kind of games do you like to play?\n1.Board games\n2.Sports games\n3.Love games\n4.Video games\n5.Python games\n6.I hate games\n7.I enjoy multiple types\n\nYour Selection: "))
		if answer_four == 1 : total_points =+ 5
		elif answer_four == 2: total_points += 5
		elif answer_four == 3: total_points += 0
		elif answer_four == 4: total_points += 2
		elif answer_four == 5: total_points += 3
		elif answer_four == 6: total_points += 0
		elif answer_four == 7: total_points += 9
		else: total_points += 0
		##Q5
		answer_five = int(input("If you were a type of cereal, what cereal would you be?\n1.Captain Crunch\n2.Frosted Flakes\n3.Fruity Pebbles\n4.Raisin Bran\n5.Special K\n6.Cinnamon Toast Crunch\n7.I hate Cereal\n8.Other\n\nYour Selection: "))
		if answer_five == 1: total_points += 5
		elif answer_five == 2: total_points += 5
		elif answer_five == 3: total_points += 20
		elif answer_five == 4: total_points += 3
		elif answer_five == 5: total_points += 2
		elif answer_five == 6: total_points += 5
		elif answer_five == 7: total_points += 0
		elif answer_five == 8: total_points += 3
		else: total_points += 0
		## q random
		answer_random  = int(input("What is your favorite color?\n 1.Blue\n 2.Blue\n 3.Green....JK, Blue\n\n Your Selection: "))
		if answer_random  == 1: total_points += 5
		elif answer_random  == 2: total_points += 5
		else: total_points += 0
		#print statement
		print(total_points)	
		break
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)


	
## Function call to play friendship algorithm game
play_game()
