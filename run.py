import os
import random


def clear():
    """
    This function clears the terminal using the os import
    """
    os.system("clear")


def update_hangman_image(values):
    """
    This function will print the hangman to the terminal and update
    it as the player makes guesses.
    """
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
    print("\t{} {}      | |".format(values[5], values[6]))
    print("\t         | |")
    print("  _______________|_|___")
    print("  `````````````````````")
    print()


def update_hangman_image_win():
    """
    this function displays the hangman image after the user sucessfully completes
    the game, printing the escaped hangman when the player wins.
    """
    print()
    print("\t +--------+")
    print("\t         | |")
    print("\t         | |")
    print("\t O       | |")
    print("\t/|\\      | |")
    print("\t |       | |")
    print("  ______/_\\______|_|___")
    print("  `````````````````````")
    print()


def print_word(values):
    """
This function will print the word to be guessed
    """

    print()
    print("\t", end="")
    for x in values:
        print(x, end="")
    print()

    """
    This function will check for a win situation.
    """


def check_win(values):
    for character in values:
        if character == '_':
            return False
        return True


def hangman_game(word):
    """
This contains the entire game functioning. It includes storing incorrect guesses,
reducing the number of chances left, and printing the specific state of hangman.
    """
    clear()

    word_display = []
    correct_letters = []
    incorrect = []
    chances = 0


topics = {1: "Random words", 2: "Famous buildings", 3: "Animals"}

dataset = {"Random words": [],
           "Famous Buildings": [],
           "Animals": []
           }
