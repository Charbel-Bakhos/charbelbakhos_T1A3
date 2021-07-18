#!/usr/bin/env python3
import time,sys,os,csv
from functions import *
from workout_routines import *



typingPrintHeading("""              ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗ ██╗   ██╗████████╗    ██████╗ ██████╗  ██████╗                
              ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝    ██╔══██╗██╔══██╗██╔═══██╗               
              ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║   ██║██║   ██║   ██║       ██████╔╝██████╔╝██║   ██║               
              ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ██║   ██║██║   ██║   ██║       ██╔═══╝ ██╔══██╗██║   ██║               
              ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗╚██████╔╝╚██████╔╝   ██║       ██║     ██║  ██║╚██████╔╝               
               ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═╝     ╚═╝  ╚═╝ ╚═════╝                """)

typingPrintText("""                                                Created by Charbel Bakhos                                               
                                                                                                                        
           Welcome to the world's top athletes best kept secret. A tried and tested workout routine selector.           
                                                                                                                        
Please follow the prompts as they come through to ensure you get a routine designed to make you big, buff and beautiful.
                                                                                                                        
                                               Press enter key to continue                                                
                                                                                                                        """)

input("")
screen_clear()
age_of_user = user_age()
if age_of_user<= 10:
    print("You should be running around outside for exercise!")
    print("There is no need yet for a structured workout regime")
    exit()
elif age_of_user < 14:
    draw_table(under14)
    exit()
elif age_of_user <18:
    draw_table(routine3day_beginner)
    exit()

sex_of_user = user_sex()
if sex_of_user == "m":
    draw_table(deadliftMale)
else:
    draw_table(deadliftFemale)

strength_of_user = user_strength()
days_of_user = user_days()

if strength_of_user == "b" and days_of_user == 3:
    draw_table(routine3day_beginner)
elif strength_of_user == "b" and days_of_user ==4:
    draw_table(routine4day_beginner)
elif strength_of_user == "b" and days_of_user ==5:
    draw_table(routine5day_beginner)
elif strength_of_user =="b" and days_of_user == 6:
    draw_table(routine6day_beginner)
elif strength_of_user == "i" and days_of_user ==3:
    draw_table(routine3day_intermediate)
elif strength_of_user == "i" and days_of_user == 4:
    draw_table(routine4day_intermediate)
elif strength_of_user == "i" and days_of_user ==5:
    draw_table(routine5day_intermediate)
elif strength_of_user == "i" and days_of_user==6:
    draw_table(routine6day_intermediate)
elif strength_of_user == "a" and days_of_user==3:
    draw_table(routine3day_advanced)
elif strength_of_user =="a" and days_of_user==4:
    draw_table(routine4day_advanced)
elif strength_of_user == "a" and days_of_user==5:
    draw_table(routine5day_advanced)
elif strength_of_user =="a" and days_of_user==6:
    draw_table(routine6day_advanced)

print("\n\nUse this workout for at least 12 weeks before changing things up!")
print("It is important to be consistent as well as hard working!!")
input("Press enter when you are ready to exit!")


