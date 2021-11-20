# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random

while 1:
    points = 0

    for x in range(10):
        randomOne = random.randint(0, 100)
        randomTwo = random.randint(0, 100)
        randomAdded = randomOne + randomTwo # The program calculates the right answer
        
        answer = int(input(f"what is {randomOne} + {randomTwo}? ")) # Asks the user for their answer
        
        if answer == randomAdded:
            print("correct\n")
            points += 1
        else:
            print(f"wrong, the right answer is {randomAdded}\n") # If the user's answer is wrong, show the correct answer.
            
    print(f"your score is: {points} out of 10") # Show the total score the user got.

# Ask the user if they want to try the "Quiz" again.
    possible_answers = ["y", "yes", "no", "n"]
    while 1:
        retry = str(input("would you like to try again? "))
        if retry in possible_answers:
            break
        else:
            print("Enter yes or no")
    if retry == "no" or retry == "n":
        break