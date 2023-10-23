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

escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")