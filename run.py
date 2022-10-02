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


def check_win(values):
    """
    This function will check for a win situation.
    """
    for character in values:
        if character == '_':
            return False
    return True


def hangman_game(word):
    """
This contains the entire game functioning. It includes storing incorrect guesses,
reducing the number of chances left, and printing the specific state of hangman.
Code snippet contains all the elementary data structures and
variables required for smooth functioning of our hangman game.
    """
    clear()

    word_display = []  # stores letters to be diplayed
    correct_letters = []  # stores the correct letters in the word
    incorrect = []  # stores all incorrect guesses
    chances = 0  # stores number of chances
    hangman_values = ['O', '/', '|', '\\', '|', '/', '\\']
    show_hangman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for character in word:  # this loop creates the display word
        if character.isalpha():
            word_display.append('_')
            correct_letters.append(character.upper())
        else:
            word_display.append(character)

    while True:  # printing values
        # connecting ith hangman values
        update_hangman_image(show_hangman_values)
        print_word(word_display)
        print()
        print("Incorrect character : ", incorrect)
        print()

        inp = input("Enter a character = ")
        if len(inp) != 1:
            clear()
            print("Please enter a valid choice!")
            continue


topics = {1: "Random words", 2: "Famous buildings", 3: "Animals"}

dataset = {"Random words": [],
           "Famous Buildings": [],
           "Animals": []
           }
