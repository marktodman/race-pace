import os
import time
import math
from math import modf


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
            self.distance = 10.0
        elif self.distance == "5km" and self.units == "km":
            self.distance = 5.0
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
        return "race_time"
    elif choice == 2:
        print("You selected 'target pace'")
        return "race_pace"
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
    Gets the runner's pace used to calculate estimated finish time.
    """
    print(f"So {name} let's calculate your esitmated {distance_str} time")
    print("To do this we need to know your running pace\n")
    print(f"How long does it take you to run 1 {unit}?\n")
    print("Please input in the format MM:SS, e.g. 06:30")
    race_pace = input(f"Enter your time for 1 {unit}: ")
    print(f"You entered {race_pace}")
    # print("Is that correct?")

    return race_pace

def get_time(name, distance_str):
    """
    Gets the runner's target finish time.
    """
    print(f"So {name} let's calculate your required pace")
    print(f"To do this we need to know your target {distance_str} finish time\n")
    print(f"What is your target time for the {distance_str}?\n")
    print("Please input in the format HH:MM:SS, e.g. 01:02:00")
    race_time = input(f"Enter your target time for the {distance_str}: ")
    print(f"You entered {race_time}")
    # print("Is that correct?")

    return race_time


def calculate_time(name, distance_str, distance_num, race_pace):
    """
    Calculates target time for given race length based on runner pace.
    """
    split_pace = race_pace.split(":")
    mins = int(split_pace[0])
    secs = int(split_pace[1])
    pace_secs = mins * 60 + secs

    race_time_secs = pace_secs * distance_num

    hours = int(race_time_secs // 3600)
    time_over = math.fmod(race_time_secs, 3600)
    float_mins = time_over / 60
    s, m = modf(float_mins)
    minutes = int(m)
    seconds = int(s * 60)
    if seconds < 10:
        sec_str = "0" + str(seconds)
    else:
        sec_str = str(seconds)
    finish_time = str(hours) + ":" + str(minutes) + ":" + sec_str
    print(f"You should complete your {distance_str} in {finish_time}\n")
    print(f"Go well in your race, {name}!")


def calculate_pace(name, distance_str, distance_num, race_time, unit):
    """
    Calculates target pace for given race length based on runner target finish time.
    """
    split_time = race_time.split(":")
    hrs = int(split_time[0])
    mins = int(split_time[1])
    secs = int(split_time[2])

    total_secs = (hrs * 3600) + (mins * 60) + secs

    pace_total_secs = total_secs / distance_num 

    pace_mins_float = pace_total_secs / 60
    s, m = modf(pace_mins_float)
    minutes = int(m)
    seconds = int(s * 60)
    if seconds < 10:
        sec_str = "0" + str(seconds)
    else:
        sec_str = str(seconds)

    target_pace = str(minutes) + ":" + sec_str
    print(f"You need to run {target_pace} per {unit} to finish in {race_time}\n")
    print(f"Go well in your race, {name}!")



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
    convert_dist = Runner.get_distance(new_runner)
    dist_converted = new_runner.distance
    race_pace_time = choose_pace_time(runner_name)
    time.sleep(1)
    cls()
    if race_pace_time == 'race_pace':
        race_pace = get_pace(runner_name, runner_distance, runner_units)
        time.sleep(1)
        cls()
        race_finish_time = calculate_time(runner_name, runner_distance, dist_converted, race_pace)
    else:
        race_time = get_time(runner_name, runner_distance)
        time.sleep(1)
        cls()
        race_finish_pace = calculate_pace(runner_name, runner_distance, dist_converted, race_time, runner_units)
    # Need to put in option to start again and exit
    # Need to validate inputs!


print("RACE PACE")
print("-" * 40)
print("Welcome to the Race Pace Calculator.")
print("We will help you smash a PR in your next race!")
main()