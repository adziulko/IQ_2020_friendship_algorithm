import sys

## Function to play friendship algorithm game  
def play_game():
    ## START GAME

    # initialize the user input to 0
    user_entry = 0
    user_entry = int(user_entry)
    # ask the user to make their own input (1 to play or 2 to exit):
    
    while user_entry != 1 and user_entry != 2: 
        user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
        user_entry = int(user_entry)
        # if the user selects 1, they want to play! Ask them questions and wait for their answers.
    
    while int(user_entry) == 1:
        
        ## Question 1 STEP 1 
        total_points= 0
        answer_one = input("Do you read books? \n1. Yes\n2. No")
        answer_one = int(answer_one)
        
        ## Question 1 STEP 2&3
        if answer_one == 1: total_points +=5
        elif answer_one == 2: total_points -=5
        else: total_points +=0

        ## Question 2 Step 1
        answer_two = input("Which do you prefer? \n1. Salad\n2. BBQ") 
        answer_two = int(answer_two)

        ## Question 2 Step 2&3
        if answer_two == 1: total_points -=5
        elif answer_two == 2: total_points +=5
        else: total_points +=0

        ## Question 3 Step 1
        answer_three = input("Where would you rather go? \n1. France\n2. Argentina\n3. Stay at home")
        answer_three = int(answer_three)

        ## Question 3 Step 2&3
        if answer_three == 1: total_points +=0
        elif answer_three == 2: total_points +=5
        else: total_points += 0

        ## Question 4 Step 1 
        answer_four = input("Which do you prefer? \n1. SKiing/Snowboarding\n2. Combat Sports\n3. Rock Climbing\n4. Stay on couch")
        answer_four = int(answer_four)

        ## Question 4 Step 2&3
        if answer_four == 1: total_points +=0
        elif answer_four == 2: total_points +=5
        elif answer_four == 3: total_points +=0
        elif answer_four == 4: total_points -=5
        else: total_points += 0

        ## Question 5 Step 1
        answer_five = input("Sweet or salty? \n1. Sweet\n2. Salty")
        answer_five = int(answer_five)

        ## Question 5 Step 2&3
        if answer_five == 1: total_points -=5
        elif answer_five == 2 : total_points +=5
        
        ## STEP 4 HERE
        print(total_points)

        if total_points > 24: print ("PERFECT SCORE")
        elif total_points > 20: print ("Let's be friends")
        elif total_points > 15: print ("We'll see...")
        elif total_points > 10: print ("I don't know about you...")
        elif total_points > 5: print ("Unlikely")
        else: print ("No way Jose")

        user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
        user_entry = int(user_entry)	


	
## Function call to play friendship algorithm game
play_game()
