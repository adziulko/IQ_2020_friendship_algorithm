import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1 :
		## STEP 1 HERE
		total_points = 0 
                answer_one = int(input('Do you want to be friends? \n1. Yes \n2. No\n\nYour Selection: '))
		## STEP 2&3 HERE
                if answer_one == 1 :
                        print('Sweet! But first, a few important questions...')
                elif answer_one == 2 :
                        print("Well...maybe later!")
                        break
                else total_points += 0
                ## Q2
                answer_two == int(input("Do you absolutely love plants??? \n1. Heck yeah! \n2. Okay maybe not /that/ much...\n\nYour Selection:"))
                if answer_two == 1 : total_points += 5
                    answer_two_one = int(input("Do you want more plants? \n1. Never too many \n2. I already have so many to take care of! \n\nYour Selection:"))
                    if answer_two_one == 1 : total_points += 5
                    elif answer_two_one == 2 : total_points += 0
                    else: total_points += 0
                elif answer_two == 2 : total_points =+ 0 
                else total_points += 0
                
                ## Q3
                answer_three == int(input("What is your favorite outdoor activity? \n1. Hiking \n2. Rockclimbing \n3. Running \n\nYour Selection:"))
                if answer_three == 1 : total_points += 5
                elif answer_three == 2 : total_points += 0
                elif answer_three == 3 : total_points -= 5
                else total_points += 0

                ## STEP 4 HERE
                print(total_points)
                if total_points == 15 : print("Let's go hike to a plant shop!") 
                elif total_points == 10 : print("We will get along just fine (:")
                elif total_points == 5 : print("Nice to meet you!")
                else: print("Well I am sure we can still make it work")
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)
	


	
## Function call to play friendship algorithm game
play_game()
