import random

#Taking Inputs
lower= int(input("ENTER THE LOWER RANGE: "))
upper= int(input("ENTER THE UPPER RANGE: "))

#Generates number with respect to the given inputs
num=random.randint(lower,upper)
total_chances=5
print("You have total 5 chances to guess the number correctly.")

#Initializing number of guesses
attempts = 0
is_correct = False

# Loop to guess the number
while attempts < total_chances:
    attempts += 1
    guess=int(input("ENTER YOUR GUESS: "))
    if guess<num:
        print("Guess Higher!")
    elif guess>num:
        print("Guess Lower!")
    elif guess==num:
        print()
    else:
        print("You're right! YOU WON!")
        is_correct = True
        break
if not is_correct:
    print(f"\nThe number was {num}")
    print("Better luck next time!")      