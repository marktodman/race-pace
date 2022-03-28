class Runner:
  """
  Defines the runner's name, distance and chosen units to be used in the calculations
  """
  
    def __init__(self, name, distance, units):
        self.name = name
        self.units = units
        
        if distance == "Marathon" and units == "km":
          self.distance = 42.195
        elif distance == "Half Marathon" and units == "km":
          self.distance = 21.0975
        elif distance == "5km" and units == "km":
          self.distance = 5.000
        elif distance == "1km" and units == "km":
          self.distance = 1.000
        elif distance == "Marathon" and units == "miles":
          self.distance = 26.2188
        elif distance == "Half Marathon" and units == "miles":
          self.distance = 13.1094
        elif distance == "5km" and units == "miles":
          self.distance = 3.106856 
        elif distance == "1km" and units == "miles":
          self.distance = 0.621371 
  
def get_user_data():
  """
  Sets up the runner, including name, distance and preferred units.
  """
  print("-" * 40)
  print("Welcome to the Race Pace Calculator.")
  print("We will help you plan to smash your next PR!")
  print("-" * 40)
  runner_name = input("Please enter your name: ")
  print("-" * 40)
  runner_distance = get_user_distance()

def get_user_distance():
  """
  Gets the runner's distance from a menu to avoid typing errors.
  """
  print("1: Marathon")
  print("2: Half Marathon")
  print("3: 5km")
  print("4: 1km")
  print("5: Exit")
  print("-" * 40)
  print(f"How far are your running?")
  print("Please input only the number for your run distance, e.g. input '1' for Marathon")
  choice = int(input("Enter your distance: "))

  if choice == 1:
    print("You selected 'Marathon' - going long!")
    return "Marathon"
  elif choice == 2:
    print("You selected 'Half Marathon'!")
    return "Half Marathon"
  elif choice == 3:
    print("You selected '5km'!")
    return "5km"
  elif choice == 4:
    print("You selected '1km'!")
    return "1km"
  elif choice == 5:
    print("OK, this programme will now exit")
    # exit()
  else:
    print("Invalid option. Please enter a number between 1 and 5.")
    print('-' * 40)
    get_user_distance()


def main():
  """
  Runs the functions for the main program.
  """

  get_user_data()

  
  
  

main()