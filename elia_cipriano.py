import sys

## Function to play friendship algorithm game
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = '0'
	i= 0

	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 'y' and i < 6:
		user_entry = str(input('Do you want to play? (y/n): '))
		if user_entry != 'y':
			print('you have to play...')
			i += 1
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 'y':
		## STEP 1 HERE
		points = 0
		step1 = str(input('\nDo you play an instrument? (y/n): '))
		if step1 == 'y':
			points += 50
		## STEP 2&3 HERE

		step2 = str(input("\nWhat's your favorite music genre?\nfunk\njazz\nrock\nrap\ncountry\n\n: ").lower())
		if step2 == 'funk':
			points += 1000
		elif step2 == 'jazz':
			points += 500
		elif step2 == 'rock':
			points += 100
		elif step2 == 'rap':
			points += 50
		elif step2 == 'country':
			points += 25

		step3 = str(input("\nDo you love the environment? (y/n): "))
		if step3 == 'y':
			points += 50
		elif step3 == 'n':
			points -= 1000

		## STEP 4 HERE
		step4 = str(input("\nDo you like butter chicken? (y/n): "))
		if step4 == 'y':
			points += 100
		elif step4 == 'n':
			points -= 100
		print('You earned ')
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)




## Function call to play friendship algorithm game
play_game()
