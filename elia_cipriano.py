import sys

## Function to play friendship algorithm game
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = '0'
	i= 0

	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 'y' and i < 6:
		user_entry = str(input('Do you want to play? (y/n): ').lower())
		if user_entry != 'y':
			print('you have to play...')
			i += 1
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 'y':
		## STEP 1 HERE
		points = 0
		step1 = str(input('\nDo you play an instrument? (y/n): ').lower())
		if step1 == 'y':
			points += 50
			print('points + 50')
		else:
			print('points + 0')
		## STEP 2 HERE
		step2 = str(input("\nWhat's your favorite music genre?\nfunk\njazz\nrock\nrap\ncountry\n\nans: ").lower())
		if step2 == 'funk':
			points += 1000
			print('points + 1000')
		elif step2 == 'jazz':
			points += 500
			print('points + 500')
		elif step2 == 'rock':
			points += 100
			print('points + 100')
		elif step2 == 'rap':
			points += 50
			print('points + 50')
		elif step2 == 'country':
			points += 25
			print('points + 25')
		else:
			print('points + 0')

		## STEP 3 HERE
		step3 = str(input("\nDo you love the environment? (y/n): ").lower())
		if step3 == 'y':
			points += 50
			print('points + 50')
		elif step3 == 'n':
			points -= 1000
			print('points -1000')
		else:
			print('points + 0')

		## STEP 4 HERE
		step4 = str(input("\nDo you like butter chicken? (y/n): ").lower())
		if step4 == 'y':
			points += 100
			print('points + 100')
		elif step4 == 'n':
			points -= 100
			print('points - 100')
		else:
			print('points + 0')

		## STEP 5 HERE (specify points)
		print('You earned {} points!'.format(points))
		if points > 1000:
			print('WE ARE BFFS!!!!')
		elif points > 0:
			print('We are friends :)')
		elif points <= 0:
			print("Uh oh.. we are not friends...")

		user_entry = str(input('Play again? (y/n): ').lower())

## Function call to play friendship algorithm game
play_game()
