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
        elif self.distance == "Marathon" and self.units == "mile":
            self.distance = 26.2188
        elif self.distance == "Half Marathon" and self.units == "mile":
            self.distance = 13.1094
        elif self.distance == "10km" and self.units == "mile":
            self.distance = 6.21371
        elif self.distance == "5km" and self.units == "mile":
            self.distance = 3.10686


def cls():
    """
    Clears the user interface.
    """

    os.system('cls' if os.name == 'nt' else 'clear')


def get_runner_name():
    """
    Gets the runner's name.
    """
    print("-" * 40)
    runner_name = input("Please enter your name: ")
    print(f"\nHi {runner_name}, please tell me more about your race...\n")
    return runner_name


def get_runner_distance(name):
    """
    Gets the runner's distance from a menu to avoid typing errors.
    """
    print(f"What distance is your race, {name}?")
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
        print("OK, the programme will now exit - BYE!")
        exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        print('-' * 40)
        # get_runner_distance()


def get_runner_units(name):
    """
    Gets the runner's choice of units - kilometers or miles - from a menu
    to avoid typing errors.
    """
    print(f"Would you prefer to use miles or kilometers, {name}?")
    print("-" * 40)
    print("1: Kilometer")
    print("2: Mile")
    print("3: Restart")
    print("4: Exit")
    print("-" * 40)
    print("Please input only the number, e.g. input '2' for miles")
    choice = int(input("Enter your preference: "))

    if choice == 1:
        print("You selected 'Kilometer'")
        return "km"
    elif choice == 2:
        print("You selected 'Mile'")
        return "mile"
    elif choice == 3:
        print("You selected 'Restart', so the program will restart")
        main()
    elif choice == 4:
        print("OK, the programme will now exit - BYE!")
        exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        print('-' * 40)


def choose_pace_time(name):
    """
    The user can choose to calculate pace for a target finish time
    or calculate a finish time based on a target pace.
    """
    print(f"Do you have a target time or target pace, {name}?")
    print("-" * 40)
    print("1: I have a target finish time")
    print("2: I have a target pace")
    print("3: Restart")
    print("4: Exit")
    print("-" * 40)
    print("Please input only the number, e.g. input '1' for target time")
    choice = int(input("Enter your preference: "))

    if choice == 1:
        print("You selected 'target finish time'")
        return "time"
    elif choice == 2:
        print("You selected 'target pace'")
        return "pace"
    elif choice == 3:
        print("You selected 'Restart', so the program will restart")
        main()
    elif choice == 4:
        print("OK, the programme will now exit - BYE!")
        exit()
    else:
        print("Invalid option. Please enter a number between 1 and 5.")
        print('-' * 40)


def get_pace(name, distance_str, unit):
    """
    Calculates the race pace required to achieve the target time.
    """
    print(f"So {name} let's calculate your {distance_str} target time")
    print("To do this we need to know your running pace\n")
    print(f"How long does it take you to run 1 {unit}?")
    print("Please input in the format MM:SS, e.g. 06:30")
    pace = input(f"Enter your time for 1 {unit}: ")

    return pace


def main():
    """
    Runs the functions for the main program.
    """
    runner_name = get_runner_name()
    time.sleep(1)
    cls()
    runner_distance = get_runner_distance(runner_name)
    time.sleep(1)
    cls()
    runner_units = get_runner_units(runner_name)
    time.sleep(1)
    cls()
    new_runner = Runner(runner_name, runner_distance, runner_units)
    convert_distance = Runner.get_distance(new_runner)
    distance_converted = new_runner.distance
    pace_time = choose_pace_time(runner_name)
    time.sleep(1)
    cls()
    pace = get_pace(runner_name, runner_distance, runner_units)

    print(runner_name)
    print(runner_distance)
    print(runner_units)
    print(distance_converted)
    print(pace_time)
    print(pace)


print("RACE PACE")
print("-" * 40)
print("Welcome to the Race Pace Calculator.")
print("We will help you smash a PR in your next race!")
main()