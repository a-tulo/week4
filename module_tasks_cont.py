import custom_functions as wk4_func
def run_week_four():
    print("Which function in 'Week 4' do you wish to run?")
    response = input()
    if response == "listen":
        wk4_func.listen()
    elif response == "create_ladder":
        wk4_func.create_ladder()


def run():

    while(True):
        print("What would you like to do?")
        print("[a] Run 'week 4' programs")
        print("[q] Quit")
        response = input()

        if response == "a":
            run_week_four()
        elif response == "q":
            break
        else:
            print("Invalid option! Please try again.")

run()