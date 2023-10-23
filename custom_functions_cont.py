# The character has now found a map, we wish to create functions that manipulate cryptic words. The program should prompt the user to enter a word. The program should then prompt the user to choose one of the following options:
#
# 1) Display in a Box – display the word in an ASCII art box
# 2) Display Lower-case – display the word in lower-case e.g. hello
# 3) Display Upper-case – display the word in upper-case e.g. HELLO
# 4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
# 5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
#
# The program should then read the option number entered by the user and carry out the appropriate actions.
#
# The program should contain 6 user-defined functions. One for each of the above options and one to run the program.
#
#
# Code your solution and be sure to include appropriate comments in your code.

def run():
    user_word = input("Enter word\n")
    user_choice = int(input('''
    1) Display in a Box – display the word in an ASCII art box
    2) Display Lower-case – display the word in lower-case e.g. hello
    3) Display Upper-case – display the word in upper-case e.g. HELLO
    4) Display Mirrored – display the word with its mirrored word e.g. Hello | olleH
    5) Repeat – ask the user how many times to display the word and then display the word that many times alternating between upper-case and lower-case.
    \n'''))

    if user_choice == 1:
        display_in_box(user_word)
    elif user_choice == 2:
        print(to_lower(user_word))
    elif user_choice == 3:
        print(to_upper(user_word))
    elif user_choice == 4:
        to_mirror(user_word)
    elif user_choice == 5:
        repeat(user_word)
def display_in_box(word):
    print(" _____")
    print(f"| {word} |")
    print(f" -----")

def to_lower(word):
    return word.lower()

def to_upper(word):
    return  word.upper()

def to_mirror(word):
    for position in range(len(word) - 1, -1, -1):
        print(word[position], end="")

def repeat(word):
    multiplier = int(input("How many times?\n"))
    print(word)
    for multiplier in range(multiplier):
        if (multiplier % 2 == 0):
            print(to_upper(word))
        else:
            print(to_lower(word))

run()