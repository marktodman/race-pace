import os
import time
import datetime
import math
from math import modf
from termcolor import colored, cprint
from pyfiglet import Figlet

headline_font = Figlet(font='speed')


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


def print_error_text(text):
    """
    Prints red on white text used in error messages.
    """
    formatted_text = colored(text, 'red', 'on_white')
    error_text = print(formatted_text)

    return error_text


def print_input_text(text):
    """
    Prints green on white text used in input confirmation messages.
    """
    formatted_text = colored(text, 'green', 'on_white')
    input_text = print(formatted_text)

    return input_text


def get_runner_name():
    """
    Gets the runner's name.
    """
    while True:
        print("-" * 40)
        runner_name = input("Please enter your first name: \n")
        if runner_name.isalpha():
            print(f"\nHi {runner_name}, please tell me more about your race...\n")
            return runner_name
        else:
            print_error_text("Invalid option. Please enter your name...\n")


def get_runner_distance(name):
    """
    Gets the runner's distance from a menu to avoid typing errors.
    """
    while True:
        print(f"What distance is your race, {name}?")
        print("-" * 40)
        print("1: Marathon")
        print("2: Half Marathon")
        print("3: 10km")
        print("4: 5km")
        print("5: Exit")
        print("-" * 40)
        print("Please input only the option number, e.g. input '4' for 5km")
        choice = ""
        try:
            choice = int(input("Enter your distance: \n"))
        except ValueError:
            print_error_text("Wrong input type...")

        if choice == 1:
            print_input_text("You selected 'Marathon' - going long!")
            return "Marathon"
        elif choice == 2:
            print_input_text("You selected 'Half Marathon'!")
            return "Half Marathon"
        elif choice == 3:
            print_input_text("You selected '10km'!")
            return "10km"
        elif choice == 4:
            print_error_text("You selected '5km'!")
            return "5km"
        elif choice == 5:
            print_error_text("OK, the program will now exit - BYE!")
            time.sleep(1)
            exit()
        else:
            print_error_text("Invalid option. Please enter a number between 1 and 5.\n")
            print('-' * 40)


def get_runner_units(name):
    """
    Gets the runner's choice of units - kilometers or miles - from a menu
    to avoid typing errors.
    """
    while True:
        print(f"Would you prefer to use miles or kilometers, {name}?")
        print("-" * 40)
        print("1: Kilometers")
        print("2: Miles")
        print("3: Restart")
        print("4: Exit")
        print("-" * 40)
        print("Please input only the number, e.g. input '2' for miles")
        choice = ""
        try:
            choice = int(input("Enter your preference: \n"))
        except ValueError:
            print_error_text("Wrong input type...")

        if choice == 1:
            print_input_text("You selected 'Kilometers'")
            return "km"
        elif choice == 2:
            print_input_text("You selected 'Miles'")
            return "mile"
        elif choice == 3:
            print_error_text("You selected 'Restart', so the program will restart")
            time.sleep(1)
            main()
        elif choice == 4:
            print_error_text("OK, the program will now exit - BYE!")
            time.sleep(1)
            exit()
        else:
            print_error_text("Invalid option. Please enter a number between 1 and 5.\n")
            print('-' * 40)


def choose_pace_time(name):
    """
    The user can choose to calculate pace for a target finish time
    or calculate a finish time based on a target pace.
    """
    while True:
        print(f"Do you have a target race time or target race pace, {name}?")
        print("-" * 40)
        print("1: I have a target finish time")
        print("2: I have a target pace")
        print("3: Restart")
        print("4: Exit")
        print("-" * 40)
        print("Please input only the number, e.g. input '1' for target time")
        choice = ""
        try:
            choice = int(input("Enter your preference: \n"))
        except ValueError:
            print_error_text("Wrong input type...")

        if choice == 1:
            print_input_text("You selected 'target finish time'")
            return "race_time"
        elif choice == 2:
            print_input_text("You selected 'target pace'")
            return "race_pace"
        elif choice == 3:
            print_error_text("You selected 'Restart', so the program will restart")
            time.sleep(1)
            main()
        elif choice == 4:
            print_error_text("OK, the program will now exit - BYE!")
            time.sleep(1)
            exit()
        else:
            print_error_text("Invalid option. Please enter a number between 1 and 5.\n")
            print('-' * 40)


def get_pace(name, distance_str, unit):
    """
    Gets the runner's pace used to calculate estimated finish time.
    """
    while True:
        timeformat = "%M:%S"
        print(f"So {name} let's calculate your estimated {distance_str} time")
        print("To do this we need to know your running pace\n")
        print(f"How long does it take you to run 1 {unit}?\n")
        print("Please input in the format M:SS or MM:SS, e.g. 6:30 or 10:05")
        race_pace = input(f"Enter your time for 1 {unit}: \n")
        try:
            valid_time = datetime.datetime.strptime(race_pace, timeformat)
            print_input_text(f"You entered {race_pace}")
            return race_pace
        except ValueError:
            print_error_text("Invalid option. Please enter time in the format MM:SS.\n")


def get_time(name, distance_str):
    """
    Gets the runner's target finish time.
    """
    while True:
        timeformat = "%H:%M:%S"
        print(f"So {name} let's calculate your required pace")
        print(f"To do this we need to know your target {distance_str} finish time\n")
        print(f"What is your target time for the {distance_str}?\n")
        print("Please input in the format H:MM:SS, e.g. 1:02:00")
        race_time = input(f"Enter your target time for the {distance_str}: \n")
        try:
            valid_time = datetime.datetime.strptime(race_time, timeformat)
            print_input_text(f"You entered {race_time}")
            return race_time
        except ValueError:
            print_error_text("Invalid option. Please enter time in the format H:MM:SS.\n")


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
    print_input_text(f"You should complete your {distance_str} in {finish_time}\n")
    print_input_text(f"Go well in your race, {name}!")
    print("-" * 40)


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
    print_input_text(f"You need to run {target_pace} per {unit} to finish in {race_time}\n")
    print_input_text(f"Go well in your race, {name}!")
    print("-" * 40)


def start_again(name):
    """
    Gives the user the option to calculate another race time or pace.
    """
    while True:
        decision = input(f"Would you like to use Race Pace for another race, {name}? Enter 'y' or 'n' ")
        if decision.isalpha():
            if decision.lower() == 'y' or decision.lower() == 'yes':
                main()
            elif decision.lower() == 'n' or decision.lower() == 'no':
                print_input_text(f"OK, {name}, thank you for using Race Pace. Go well!")
                print_error_text("Race Pace will now exit...")
                time.sleep(3)
                exit()
            else:
                print_error_text("Invalid option. Please enter 'y' or 'n'...\n")
        else:
            print_error_text("Invalid option. Please enter 'y' or 'n'...\n")


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
    time.sleep(3)
    start_again(runner_name)


print(colored(headline_font.renderText("RACE PACE"), 'green', 'on_white'))
print("-" * 40)
print("Welcome to the Race Pace Calculator.")
print("We will help you smash a PR in your next race!")
main()
