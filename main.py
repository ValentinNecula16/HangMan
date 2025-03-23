import random
from hangman_words import word_list
from hangman_art import logo, stages

lives = 6


print(logo)

chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    else:
        correct_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")


    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    if lives == 0:
        print(f"IT WAS {chosen_word.upper()}! YOU LOSE")
        game_over = True
