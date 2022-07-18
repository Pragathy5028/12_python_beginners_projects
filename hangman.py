import random
from words import words
import string

lives=6

word=random.choice(words).upper()

letters_in_word=set(word)
alphabet=set(string.ascii_uppercase)
used_letters=set()

# getting user input
while len(letters_in_word)>0 and lives >0:

    print(f"You have {lives} live/s left and have used these letter : "," ".join(used_letters))
    # what the current word is
    word_list = [letter if letter in used_letters else "_" for  letter in word]
    print("Current word : ", " ".join(word_list))

    user_letter=input("Guess the letter: ").upper()
    if user_letter in alphabet:
        used_letters.add(user_letter)
        if user_letter in letters_in_word:
            letters_in_word.remove(user_letter)
        else:
            lives=lives-1 #takes away a life if guess is wrong
    elif user_letter in used_letters:
        print("You have already used that character.Please try again.")

    else:
        print("Invalid character")


if lives==0:
    print(f"Sorry.You died. The word was {word}")
else:
    print(f"You guessed the word {word} !!!")

