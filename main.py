import random 

from hangman_words import word_list
from hangman_art import *

chosen_word = random.choice(word_list)
lives = 6

display = []
#for each letter in chosen_word add an "_" to display.
for letter in chosen_word:
    display += "_"

playing = True

print(logo)

while playing:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print("You've already guessed that letter.")
        
    #If the letter at that position matches 'guess' then replace that letter in the display at that position.

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the chosen word. You lose a life.")
        lives -= 1
    if lives == 0:
        playing = False
        print("You Lose!")

    if "_" not in display:
        playing = False
        print("You Win")

    print(display)
    print(images[lives])
        
