import random

min_val = int(input("Please enter the minimum value:  "))
max_val = int(input("Please enter the maximum value:  "))

def play_game(min,max):
    game_complete = False
    target_num = random.randint(min_val, max_val)

    while game_complete == False:
        usr_guess = int(input(f"I am thinking of a number between {min} and {max}. Can you guess what it is?\n"))
        if usr_guess < target_num:
            print("Too low")
        elif usr_guess > target_num:
            print("Too high")
        elif usr_guess == target_num:
            print("Congratulations! You guessed my number")
            game_complete = True

play_game(min_val, max_val)


