# Syeda Khunza Fatima
# Emmanuel Cruz
# oct 29, 2024

# generate the random number from 1-25
# loop to allow user to guess
# prompt the user to enter a guess
# covert users input to integers
# guess the higher number
# if you guessed it right then you won


import random

# Step 1: generate the random number from 1-25
random_number = random.randint(1, 25)

print("Welcome to the Number Guessing Game!")
print("I have generated a random number between 1 and 25. Try to guess it!")

# Step 2: Loop to allow user to guess
while True:
    # Step 3: prompt the user to enter a guess
    user_input = input("Enter your guess: ")
    
    # Step 4: convert user's input to integers
    try:
        user_guess = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue
   
    # Step 5: Guess the higher number
    if user_guess < 1 or user_guess > 25:
        print("Your guess is out of bounds! Please guess a number between 1 and 25.")
    else:
       
        if user_guess == random_number:
            # Step 6: if you guessed it right then you won
            print("Congratulations! You guessed it right. The number was", random_number)
            break  
        elif user_guess < random_number:
            print("Your guess is too low! Try guessing a higher number.")
        else:
            print("Your guess is too high! Try guessing a lower number.")
