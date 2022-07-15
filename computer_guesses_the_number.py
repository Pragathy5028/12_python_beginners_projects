import random


high=int(input("Enter the upper bound : "))
low=1
guess=0
feedback=""
guess_count=0
while feedback!='c':
    guess_count+=1
    if low !=high:
        guess=random.randint(low,high)
    else:
        guess=low #could also be high since low =high
    feedback=input(f"If the {guess} is too high(H),too low(L) or correct(C) : ").lower()
    if feedback=="h":
        high=guess-1
    elif feedback=='l':
        low=guess+1
print(f"Yaay!!The computer guessed the number{guess}correctly!")
print(f"The computer made {guess_count} guesses")