import os
import time
import datetime
from math import modf, fmod
from termcolor import colored, cprint
from pyfiglet import Figlet

headline_font = Figlet(font='speed')


class Runner:
    """
    Defines the runner's distance as an integer based on users
    distance and units preference to be used in the calculator.
    """
    def __init__(self, distance, units):
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


def error_text(text):
    """
    Prints red on white text used in error messages.
    """
    formatted_text = colored(text, 'red', 'on_white')
    error_text = print(formatted_text)

    return error_text


def input_text(text):
    """
    Prints blue on white text used in input confirmation messages.
    """
    formatted_text = colored(text, 'blue', 'on_white')
    input_text = print(formatted_text)

    return input_text


def output_text(text):
    """
    Prints green on white text used in input confirmation messages.
    """
    formatted_text = colored(text, 'green', 'on_white')
    output_text = print(formatted_text)

    return output_text


def runner_name():
    """
    Gets the runner's name.
    """
    while True:
        print("-" * 40)
        runner_name = input("Please enter your first name: \n")
        if runner_name.isalpha():
            input_text(f"\nHi {runner_name} please tell me about your race\n")
            return runner_name
        else:
            error_text("Invalid option. Please enter your name...\n")
            time.sleep(1)
            cls()


def runner_distance(name):
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
        print("Please input only the option number, e.g. input '4' for 5km.")
        choice = ""
        try:
            choice = int(input("Enter your distance: \n"))
        except ValueError:
            error_text("Wrong input type...")

        if choice == 1:
            input_text("You selected 'Marathon' - going long!")
            return "Marathon"
        elif choice == 2:
            input_text("You selected 'Half Marathon'!")
            return "Half Marathon"
        elif choice == 3:
            input_text("You selected '10km'!")
            return "10km"
        elif choice == 4:
            input_text("You selected '5km'!")
            return "5km"
        elif choice == 5:
            error_text("OK, Race Pace will now exit - BYE!")
            time.sleep(1)
            cls()
            exit()
        else:
            error_text("Invalid. Please enter a number between 1 and 5.")
            time.sleep(1)
            cls()


def runner_units(name):
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
        print("Please input only the number, e.g. input '2' for miles.")
        choice = ""
        try:
            choice = int(input("Enter your preference: \n"))
        except ValueError:
            error_text("Wrong input type...")

        if choice == 1:
            input_text("You selected 'Kilometers'")
            return "km"
        elif choice == 2:
            input_text("You selected 'Miles'")
            return "mile"
        elif choice == 3:
            error_text("You selected 'Restart', so the program will restart.")
            time.sleep(1)
            main()
        elif choice == 4:
            error_text("OK, Race Pace will now exit - BYE!")
            time.sleep(1)
            cls()
            exit()
        else:
            error_text("Invalid. Please enter a number between 1 and 5.")
            time.sleep(1)
            cls()


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
        print("Please input only the number, e.g. input '1' for target time.")
        choice = ""
        try:
            choice = int(input("Enter your preference: \n"))
        except ValueError:
            error_text("Wrong input type...")

        if choice == 1:
            input_text("You selected 'target finish time'")
            return "race_time"
        elif choice == 2:
            input_text("You selected 'target pace'")
            return "race_pace"
        elif choice == 3:
            error_text("You selected 'Restart', so the program will restart.")
            time.sleep(1)
            main()
        elif choice == 4:
            error_text("OK, Race Pace will now exit - BYE!")
            time.sleep(1)
            cls()
            exit()
        else:
            error_text("Invalid. Please enter a number between 1 and 5.")
            time.sleep(1)
            cls()


def get_pace(name, distance_str, unit):
    """
    Gets the runner's pace used to calculate estimated finish time.
    """
    while True:
        timeformat = "%M:%S"
        print(f"So {name} let's calculate your estimated {distance_str} time.")
        print("To do this we need to know your running pace.\n")
        print(f"How long does it take you to run 1 {unit}?\n")
        print("Please input in the format M:SS or MM:SS, e.g. 6:30 or 10:05.")
        race_pace = input(f"Enter your time for 1 {unit}: \n")
        try:
            valid_time = datetime.datetime.strptime(race_pace, timeformat)
            input_text(f"You entered {race_pace}")
            return race_pace
        except ValueError:
            error_text("Invalid. Please use the format M:SS or MM:SS.\n")
            time.sleep(1)
            cls()


def get_time(name, distance_str):
    """
    Gets the runner's target finish time.
    """
    while True:
        timeformat = "%H:%M:%S"
        print(f"So {name} let's calculate your required pace.")
        print("To do this we need to know your target finish time.\n")
        print(f"What is your target finish time for the {distance_str}?\n")
        print("Please input in the format H:MM:SS, e.g. 1:02:00 or 0:44:59.")
        race_time = input(f"Enter your target time for the {distance_str}: \n")
        try:
            valid_time = datetime.datetime.strptime(race_time, timeformat)
            input_text(f"You entered {race_time}")
            return race_time
        except ValueError:
            error_text("Invalid. Please enter time in the format H:MM:SS.\n")
            time.sleep(1)
            cls()


def calc_time(name, distance_str, distance_num, race_pace, unit):
    """
    Calculates target time for given race length based on runner pace.
    """
    split_pace = race_pace.split(":")
    mins = int(split_pace[0])
    secs = int(split_pace[1])
    pace_secs = mins * 60 + secs

    race_time_secs = pace_secs * distance_num

    hours = int(race_time_secs // 3600)
    time_over = fmod(race_time_secs, 3600)
    float_mins = time_over / 60
    s, m = modf(float_mins)
    minutes = int(m)
    if minutes < 10:
        min_str = "0" + str(minutes)
    else:
        min_str = str(minutes)
    seconds = int(s * 60)
    if seconds < 10:
        sec_str = "0" + str(seconds)
    else:
        sec_str = str(seconds)
    finish_time = str(hours) + ":" + min_str + ":" + sec_str

    output_text(f"If you run at a pace of {race_pace} per {unit}")
    output_text(f"You should complete your {distance_str} in {finish_time}")


def calc_pace(name, distance_str, distance_num, race_time, unit):
    """
    Calculates target pace for race length based on runner target finish time.
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
    if minutes < 10:
        min_str = "0" + str(minutes)
    else:
        min_str = str(minutes)
    seconds = int(s * 60)
    if seconds < 10:
        sec_str = "0" + str(seconds)
    else:
        sec_str = str(seconds)

    target_pace = min_str + ":" + sec_str
    output_text(f"To acheive your target finish time of {race_time}")
    output_text(f"You need to run {target_pace} per {unit}")

    return target_pace


def calc_split_dist(dist_num, dist_str):
    """
    Calculates the runner's split distances based on the race length.
    """
    split_dist = []

    if dist_str == 'Marathon':
        num_splits = int(dist_num // 3)
        split_dist = [(i * 3 + 3) for i in range(num_splits)]
    elif dist_str == 'Half Marathon':
        num_splits = int(dist_num // 2)
        split_dist = [(i * 2 + 2) for i in range(num_splits)]
    else:
        num_splits = int(dist_num // 1)
        split_dist = [(i + 1) for i in range(num_splits)]

    return split_dist


def calc_split_time(split_dist, pace):
    """
    Calculates the split times for the runner's pace over the race distance.
    """
    split_time = []

    for i in split_dist:
        split_pace = pace.split(":")
        mins = int(split_pace[0])
        secs = int(split_pace[1])
        pace_secs = mins * 60 + secs

        time_to_split = pace_secs * i

        hours = int(time_to_split // 3600)
        time_over = fmod(time_to_split, 3600)
        float_mins = time_over / 60
        s, m = modf(float_mins)
        minutes = int(m)
        if minutes < 10:
            min_str = "0" + str(minutes)
        else:
            min_str = str(minutes)
        seconds = int(s * 60)
        if seconds < 10:
            sec_str = "0" + str(seconds)
        else:
            sec_str = str(seconds)
        split = str(hours) + ":" + min_str + ":" + sec_str
        split_time.append(split)

    return split_time


def splits(split_dist, split_time, dist_str, unit, name):
    """
    Present split times for distances related to race distance.
    """
    print(f"Here are some splits to help with your {dist_str} pacing.")
    print(f"You should be passing these {unit} markers at these times:\n")
    print(f"{unit} // split time")

    splits = dict(zip(split_dist, split_time))
    for distance, time in splits.items():
        print(distance, time)

    output_text(f"Go well in your race, {name}!")
    print("-" * 40)


def start_again(name):
    """
    Gives the user the option to calculate another race time or pace.
    """
    while True:
        print(f"Would you like to use Race Pace again, {name}?")
        decision = input("Enter 'y' or 'n' \n")
        if decision.isalpha():
            if decision.lower() == 'y' or decision.lower() == 'yes':
                output_text(f"OK, {name}, Race Pace will start over!")
                time.sleep(1)
                cls()
                run_again(name)
            elif decision.lower() == 'n' or decision.lower() == 'no':
                output_text(f"OK, {name}, thank you for using Race Pace!")
                error_text("Race Pace will now exit...")
                time.sleep(3)
                cls()
                exit()
            else:
                error_text("Invalid. Please enter 'y' or 'n'...\n")
        else:
            error_text("Invalid. Please enter 'y' or 'n'...\n")


def run_again(name):
    """
    Runs the program again without the name needing to be input
    """
    r_name = name
    r_dist = runner_distance(r_name)
    time.sleep(1)
    cls()
    r_units = runner_units(r_name)
    time.sleep(1)
    cls()
    new_runner = Runner(r_dist, r_units)
    convert_dist = Runner.get_distance(new_runner)
    dist_conv = new_runner.distance
    race_pace_time = choose_pace_time(r_name)
    time.sleep(1)
    cls()
    if race_pace_time == 'race_pace':
        race_pace = get_pace(r_name, r_dist, r_units)
        time.sleep(1)
        cls()
        race_f_time = calc_time(r_name, r_dist, dist_conv, race_pace, r_units)
    else:
        race_time = get_time(r_name, r_dist)
        time.sleep(1)
        cls()
        race_pace = calc_pace(r_name, r_dist, dist_conv, race_time, r_units)
    split_dist = calc_split_dist(dist_conv, r_dist)
    split_time = calc_split_time(split_dist, race_pace)
    race_splits = splits(split_dist, split_time, r_dist, r_units, r_name)
    time.sleep(5)
    start_again(r_name)


def main():
    """
    Runs the functions for the main program.
    """
    r_name = runner_name()
    time.sleep(1)
    cls()
    r_dist = runner_distance(r_name)
    time.sleep(1)
    cls()
    r_units = runner_units(r_name)
    time.sleep(1)
    cls()
    new_runner = Runner(r_dist, r_units)
    convert_dist = Runner.get_distance(new_runner)
    dist_conv = new_runner.distance
    race_pace_time = choose_pace_time(r_name)
    time.sleep(1)
    cls()
    if race_pace_time == 'race_pace':
        race_pace = get_pace(r_name, r_dist, r_units)
        time.sleep(1)
        cls()
        race_finish = calc_time(r_name, r_dist, dist_conv, race_pace, r_units)
    else:
        race_time = get_time(r_name, r_dist)
        time.sleep(1)
        cls()
        race_pace = calc_pace(r_name, r_dist, dist_conv, race_time, r_units)
    split_dist = calc_split_dist(dist_conv, r_dist)
    split_time = calc_split_time(split_dist, race_pace)
    race_splits = splits(split_dist, split_time, r_dist, r_units, r_name)
    time.sleep(3)
    start_again(r_name)


print(colored(headline_font.renderText("RACE PACE"), 'green', 'on_white'))
print("-" * 40)
print("Welcome to the Race Pace Calculator.")
print("Race Pace helps you achieve a goal finish time in your race.")
print("Whether that is a Marathon, Half Marathon, 10km or 5km.")
print("Let's plan to smash a PR in your next race!")
main()
