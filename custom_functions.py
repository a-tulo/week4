def listen():
    user_sound = input("Enter a word representing a sound\n")
    print(f"That was a loud {user_sound}!")

def identify():
    user_vision = input("What do you see?\n")
    if user_vision == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")

def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that wsy! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")

def cross_bridge(distance):
    for i in range(distance):
        print("Crossed step")
    if distance > 5:
        print("The bride is collapsing!")
    else:
        print("We must keep going")

def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still some way to go!")
    else:
        print("We are almsot there!")

def display_ladder(steps):
    print(''' 
    | |
    ***
    ''' * steps) #cheat way of doing it. Solutions says For step in range(steps): print statements.
    print("| |") # bottom of ladder

def create_ladder():
    user_steps = int(input("How many steps remain?\n"))
    display_ladder(user_steps)

