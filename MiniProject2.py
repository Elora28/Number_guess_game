import random

number = random.randint(1, 100)   # pick a random number
attempts = 0                      # start counting at 0
guess = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    attempts = attempts + 1       # add 1 each time

    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct!")

print("You used", attempts, "attempts") 
# this is a comment
