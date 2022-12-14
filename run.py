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
    This function will check if the word guessed is = to one of the hidden letters and if so update the appropriate section of the game
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
            word_display.append(' _ ')
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

        if not inp[0].isalpha():
            clear()
            print("Please enter a valid choice!")
            continue

        if inp.upper() in incorrect:  # prints statement if letter has already been guessed
            clear()
            print("Already tried")
            continue

        if inp.upper() not in correct_letters:

            # adds incorrect guesses to guessed lisst
            incorrect.append(inp.upper())

            show_hangman_values[chances] = hangman_values[chances]
            chances = chances + 1

            if chances == len(hangman_values):
                print()
                clear()
                print("\tYOU TRIED YOUR BEST, GAME OVER!")
                # hangman value funtion updated
                update_hangman_image(hangman_values)
                print("The word is :", word.upper())
                break

        else:
            # Updating the word display
            for i in range(len(word)):
                if word[i].upper() == inp.upper():
                    word_display[i] = inp.upper()  # everything added in uppercase

            if check_win(word_display):  # checks for win condition
                clear()
                print("\tCongratulations! ")
                update_hangman_image_win()
                print("The word is :", word.upper())  # diplays finished word
                break
        os.system("clear")

if __name__ == "__main__":
    os.system("clear")

    topics = {1: "Random words", 2: "Animals"}

    dataset = {"Random words": ["aback","abaft","abandoned",
            "abashed","aberrant","abhorrent","aboard","aboriginal","abortive",
            "abounding","abrasive","abrupt","absent","absorbed","absorbing","abstracted",
            "absurd","abundant","abusive","acceptable","accessible",
            "accidental","accurate","disagreeable",
            "disastrous","discreet","disgusted","disgusting","disillusioned","scandalous","scarce",
            "scared","scary","scattered","scientific","scintillating","scrawny","zealous",
            "zesty","zippy", "recess","record","regret","relation",
            "religion","representative","request",],
            "Animals": ["Tiger", "Elephant", "Polar bear", "Leaopard",
                        "Emu", "Great white shark", "Deer"
                        "Giraffe", "Archaeopteryx", "Bullmastiff", "Devils coach horse beetle" ]
            }

    while True: #start of game loop
        print("-----------------------------------------")
        print("\t\tGAME MENU")
        print("-----------------------------------------")
        for key in topics:
            print("Press", key, "to select", topics[key])
        print("press", len(topics)+1, "to quit")
        print()
        try:
            choice = int(input("Enter your choice here = "))
        except ValueError:
            clear()
            print("Invalid choice, please select again!")
            continue
        if choice > len(topics)+1:
            clear()
            print("Not that many topics! Please select again")
            continue
        if choice == len(topics)+1:
            print()
            print("Thanks for playing!Come back again some time :) ")
            break
        chosen_topic = topics[choice]
        ran = random.choice(dataset[chosen_topic])
        hangman_game(ran)
        
