import os
import time


class Runner:
    """
    Defines the runner's name, distance and chosen units
    to be used in the calculator.
    """
    def __init__(self, name, distance, units):
        self.name = name
        self.units = units
        self.distance = distance

    def get_distance(self):
        if self.distance == "Marathon" and self.units == "km":
            self.distance = 42.195
        elif self.distance == "Half Marathon" and self.units == "km":
            self.distance = 21.0975
        elif self.distance == "10km" and self.units == "km":
            self.distance = 10.000
        elif self.distance == "5km" and self.units == "km":
            self.distance = 5.000
        elif self.distance == "Marathon" and self.units == "miles":
            self.distance = 26.2188
        elif self.distance == "Half Marathon" and self.units == "miles":
            self.distance = 13.1094
        elif self.distance == "10km" and self.units == "miles":
            self.distance = 6.21371
        elif self.distance == "5km" and self.units == "miles":
            self.distance = 3.10686


def cls():
    """
    Clears the user interface.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def get_runner_name():
    """
    Sets up the runner, including name, distance and preferred units.
    """
    print("-" * 40)
    runner_name = input("Please enter your name: ")
    print(f"\nHi {runner_name}, please tell me more about your race...\n")
    time.sleep(1)
    cls()
    return runner_name


def get_runner_distance(name):
    """
    Gets the runner's distance from a menu to avoid typing errors.
    """
    print(f"{name}, what distance is your race?")
    print("-" * 40)
    print("1: Marathon")
    print("2: Half Marathon")
    print("3: 10km")
    print("4: 5km")
    print("5: Exit")
    print("-" * 40)
    print("Please input only the option number, e.g. input '4' for 5km")
    choice = int(input("Enter your distance: "))

    if choice == 1:
        print("You selected 'Marathon' - going long!")
        return "Marathon"
    elif choice == 2:
        print("You selected 'Half Marathon'!")
        return "Half Marathon"
    elif choice == 3:
        print("You selected '10km'!")
        return "10km"
    elif choice == 4:
        print("You selected '5km'!")
        return "5km"
    elif choice == 5:
        print("OK, this programme will now exit")
        # exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        print('-' * 40)
        get_user_distance()


def get_runner_units():
    pass
    """
    Gets the runner's choice of units - kilometers or miles - from a menu
    to avoid typing errors.
    """
    print("Would you prefer to use miles or kilometers?")
    print("1: Kilometers")
    print("2: Miles")
    print("3: Restart")
    print("4: Exit")
    print("-" * 40)
    print("Please input only the number, e.g. input '2' for miles")
    choice = int(input("Enter your preference: "))

    if choice == 1:
        print("You selected 'Kilometers'")
        return "km"
    elif choice == 2:
        print("You selected 'Miles'")
        return "miles"
    elif choice == 3:
        print("You selected 'Restart', so the program will restart")
        get_user_data()
    elif choice == 4:
        print("OK, this programme will now exit")
        # exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        print('-' * 40)
        get_user_distance()


def choose_pace_time():
    pass
    """
    The user can choose to calculate pace for a target finish time
    or calculate a finish time based on a target pace.
    """
    distance = user_data[1]
    print(distance)


def main():
    """
    Runs the functions for the main program.
    """
    runner_name = get_runner_name()
    runner_distance = get_runner_distance(runner_name)
    # convert_distance = Runner.get_distance(runner) # create distance as an int
    # distance = runner.distance
    # choose_pace_time()
    print(runner_name)
    print(runner_distance)


print("RACE PACE")
print("-" * 40)
print("Welcome to the Race Pace Calculator.")
print("We will help you smash a PR in your next race!")
main()