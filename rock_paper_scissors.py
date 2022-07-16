import random

options=["rock","paper","scissors"]
user_points=0
computer_points=0

while True:
    user_pick=input("Enter rock,paper,scissors or q to quit: ")
    computer_pick=random.choice(options)
    print(f"The computer choose {computer_pick}")


    if user_pick=="q":
        break
    elif user_pick not in options:
        continue
    elif user_pick==computer_pick:
        print("Its a tie") 
    elif (user_pick=="rock"and computer_pick=="paper")or(user_pick=="paper"and computer_pick=="scissors")\
        or(user_pick=="scissors"and computer_pick=="rock"):
        user_points+=1
        
        print("You won!")
    else:
        computer_points+=1
        print("computer won!")
    
print(f"You won {user_points} time/s")
print(f"Computer won {computer_points} time/s")