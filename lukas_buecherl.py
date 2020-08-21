import sys

## Handle answer
def test(answer):
	try:
		answer.lower() == 'yes' or answer == 'no'
	except:
		print("You did not answer the question! Type y for yes and n for no.")
	finally:
		return(answer)

def test_beer(answer):
	try:
		answer.lower() == 'weissbier' or answer == 'helles'
	except:
		print("You did not answer the question! Type either Weissbier or Helles.")
	finally:
		return(answer)

## Function to play friendship algorithm game
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):

	while user_entry != 1 and user_entry != 2:
		try:
			user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
		except:
			print('Ooops... Something went wrong. Please type 1 to play and 2 to quit.')

	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while int(user_entry) == 1:
		## STEP 1 HERE
		total_points= 0
		answer_one = test(input("Do you like coding? Just answer with yes or no. \n Your Answer: "))

		print(answer_one)
		print(type(answer_one))
		if answer_one == 'yes': total_points +=5
		elif answer_one == 'no': total_points -=5
		else: total_points +=0

		## STEP 2 HERE
		answer_two = test(input("Do you believe in climate change? Answer with yes or no. \n Your Answer: "))
		if answer_two == 'yes': total_points +=5
		elif answer_two == 'no': total_points -=10
		else: total_points +=0

		## STEP 3 HERE
		answer_three = test(input("Do you have knowledge of beer? Answer with yes or no. \n Your Answer: "))
		if answer_three == 'yes': total_points +=10
		elif answer_three == 'no': total_points -=5
		else: total_points +=0

		## STEP 4 HERE
		if answer_three == 'yes':
			answer_four = test_beer(input("Do you prefer Weissbier or Helles?  \n1. Weissbier\n2. Helles\nYour Selection: "))
			if answer_four == 'Weissbier': total_points +=8
			elif answer_four == 'Helles': total_points +=3
			else: total_points +=0

		## STEP 5 HERE
		answer_five = test(input("Do you like the Beatles? Answer with yes or no. \n Your Answer: "))
		if answer_five == 'yes': total_points +=10
		elif answer_five == 'no': total_points -=5
		else: total_points +=0

		## FINAL STEP
		print(total_points)
		if total_points > 37: print("You are probably me")
		elif total_points > 32: print("We can definetly be friends")
		elif total_points > 15: print("We can work this out")
		elif total_points > 10: print("Gonna be tough not gonna lie")
		elif total_points > 5: print("Let's start from the bottom")
		else: print("Well no")


		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)




## Function call to play friendship algorithm game
play_game()
