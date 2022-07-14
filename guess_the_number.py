import random


answer=input("Welcome to number guessing game.Do you wanna play?").lower()
if answer!="yes":
    print("See you later then.")
    quit()
upper_bound=input("Enter a number: ")

if upper_bound.isdigit():
    upper_bound=int(upper_bound)
    if upper_bound<0:
        print("Enter a positive number next time")
        quit()
else:
    print("Enter a number next time")
    quit()

guesses=0
random_number=random.randint(1,upper_bound)
while True:
    guesses+=1
    user_guess=input("Make a guess:")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Enter a number next time")
        continue
    if user_guess==random_number:
        print("You got it right!")
        break
    elif user_guess>random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")


print(f"You made {guesses} guesses.")
