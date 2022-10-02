import os
import random


def clear():
    """
    This function clears the terminal using the os import
    """
    os.system("clear")


def update_hangman_image(values):
    print()
    print("\t +--------+")
    print("\t |       | |")
    print("\t {}       | |".format(values[0]))
    print("\t{}{}{}      | |".format(values[1], values[2], values[3]))
    print("\t {}       | |".format(values[4]))
