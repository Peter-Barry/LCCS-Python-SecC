# Question 16(b)
# Examination Number:

from random import randint
user_score = 0 # a variable to keep track of the user's score

# Keep looping until the break statement is executed ...
# ... this will happen when the does not wish to play another round
while True:

    secret_number = randint(1, 100) # generate the secret number
    user_guess = int(input("Enter your guess: ")) # get the user's guess

# calculate the absolute difference between the user's guess and the secret number
    difference = abs(user_guess-secret_number)
    print("Secret number is %d. You guessed %d. Difference is %d" %(secret_number,user_guess, difference))

# Calculate the score based on how close the user's guess is to the secretnumber ...
# ... the closer the guess the more points the user/player gets
    if user_guess == secret_number: # both numbers are the same ...
        user_score += 100 # ... increase the score by 100 and ...
        print("JACKPOT!!! You score 100 points") # ... tell the user
    elif difference < 20: # if the difference is less than 20 ...
        user_score += 20 # ... increase the score by 20 and ...
        print("You score 20 points") # ... tell the user
    elif difference > 30: # if the difference is more than 30 ...
        user_score -= 30 # ... decrease the score by 30 and ...
        print("Your lose 30 points") # ... tell the user

# display a message with the total score at the end of each round
    print("Your total score is:", user_score)

    play_again = input("Play again? (y/n): ") # prompt the user to play again
    if play_again.lower() != "y":
        break 