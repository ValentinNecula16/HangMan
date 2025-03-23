# HangMan

This is a Python-based implementation of the classic Hangman game. The player needs to guess a randomly chosen word by suggesting letters. For each incorrect guess, a part of the hangman figure is drawn. The game ends when the player either guesses the word correctly or the hangman is fully drawn, indicating the player has lost.

## Features

- Random word selection from a predefined word list.
- Interactive command-line interface where the player guesses letters.
- Displays hangman stages as the player loses lives.
- Keeps track of the number of lives remaining.
- Notifies the player of previously guessed letters.
- Congratulates the player upon winning or displays the correct word when losing.

## Requirements

To run this game, you need to have Python installed on your system. The game was developed using Python 3.

## Game Play

- The game starts by displaying a logo and the word to guess represented by underscores.
- The player can guess one letter at a time.
- If the letter is part of the word, it is revealed in its correct position.
- If the letter is not part of the word, one life is deducted and a part of the hangman figure is drawn.
- The player has 6 lives before the game ends.
- The game continues until the word is guessed or the player loses all lives.
