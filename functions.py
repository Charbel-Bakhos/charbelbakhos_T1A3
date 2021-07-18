import time, sys, os, csv
from workout_routines import *

#This is to run the large ascii heading as a typing out animation
def typingPrintHeading(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)

#This is to run the text below heading as a typing out animation but slower
def typingPrintText(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.005)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.01)
  value = input()  
  return value

def screen_clear():
  # for mac and linux(here, os.name is 'posix')
  if os.name == 'posix':
    _ = os.system('clear')
  else:
    # for windows platfrom
    _ = os.system('cls')

#This function is to draw up the tables, it fetches data from the csv files which contain the 
#Workout routines
def draw_table(routine):
    screen_clear()
    data = []
    for row in routine:
      data.append(row)
    header = data.pop(0)
    print("#" * 101)
    print("# " ,end=" ")
    for column in header:
        print(fixed_length(column,20), end = "  #  ")
    print()
    print("#" * 101)
    for row in data:
        print("# " ,end=" ")
        for column in row:
            print(fixed_length(column,20), end = "  #  ")
        print()
    print("#" * 101)

#This function keeps the columns in the table at a certain length
def fixed_length(text,length):
    if len(str(text)) > length:
        text = text[:length]
    elif len(str(text)) < length:
        text = (text + " " * length)[:length]
    return text

#This function gets the users age
def user_age():
  age = 0
  while age <= 0 or age >= 122:
    try:
      age = int(input("What is your age in years? "))
      if age >=122:
        print("Congratulations! You are officially the oldest person in the world :) ")
      elif age <=0:
        print("You are yet to be born however know how to use Python! Ahead of the game :)")
    except ValueError:
      print("That is not a number! Try again ")
  return age
#This function gets the users sex
def user_sex():
  sex = ""
  while not sex.lower() == "m" or not sex.lower() == "f":
    try:
      sex= input("What is your sex? M or F: ")
      if sex.lower() == "m" or sex.lower() == "f":
        break  
      else:
        print("Please try again! ")
    except:
      print("Please only select M or F ")
  return sex.lower()
#This function gets how many days per week the user wants to workout
def user_days():
  days = ""
  print("How many days per week would you like to train?")
  while  days not in range(3,7):
    try:
      days = int(input("Please select between 3 and 6 days: "))
      if days not in range(3,7):
        print("That is not between 3 to 6 days!!!")
    except ValueError:
      print("That is not a number! ")
  return days

#This function will allow the user to select their strength levels.
def user_strength():
  print("""▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▄ █▄ ▄█ ▄▄▀█ ▄▄█ ▄▄▀█ ▄▄▄█▄ ▄█ ███████ ▄▄▄ █▄ ▄█ ▄▄▀█ ▄▄▀█ ▄▀█ ▄▄▀█ ▄▄▀█ ▄▀█ ▄▄
██▄▄▄▀▀██ ██ ▀▀▄█ ▄▄█ ██ █ █▄▀██ ██ ▄▄ ████▄▄▄▀▀██ ██ ▀▀ █ ██ █ █ █ ▀▀ █ ▀▀▄█ █ █▄▄▀
██ ▀▀▀ ██▄██▄█▄▄█▄▄▄█▄██▄█▄▄▄▄██▄██▄██▄████ ▀▀▀ ██▄██▄██▄█▄██▄█▄▄██▄██▄█▄█▄▄█▄▄██▄▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
  strength = ""
  print("\nNote, all values are in kilograms.\n")
  print("""First, take a look at the first column and find the bodyweight closest to your own.
Then trace to the right until you find the maximum weight you can lift.
Then trace upwards so you can see your strength level!""")
  print("""If you are unsure how much weight you can lift, or have just started working out
please select Beginner in the next step!\n""")
  while strength.lower() != "b" or strength.lower() != "i" or strength.lower() != "a":
    try:
      strength = input("Please select your strength level by typing 'B', 'I' or 'A': ")
      if strength.lower() == "b" or strength.lower() == "i" or strength.lower() == "a":
        break
      else:
        print("Please try again!")
    except:
      print("Please only select B, I or A")
  return strength.lower()
