### Charbel Bakhos
### T1A3 - Terminal Application

# Software Development Plan


## Statement of Purpose and Scope
One of the most common problems I identify in individuals when they request help with going to the gym is that they don't have a structured routine. Structure in your workouts creates good habits, the ability to identify and work on weaknesses, and catering to the individual.

This application is developed with the above in mind and aims to help beginners all the way to advanced athletes select their gym routine. The reason this is being developed is to reduce stress in planning workouts so the individual can focus on the actual training. 

The application will take user input in the form of:
* Age
* Sex
* Strength levels
* How many days a week they would like to train

Using these inputs it will cater to the user and select a workout routine tailored to their needs.

## Features
### User input for Age, Strength and days per week
This feature will use functions to get a users age, strength and how many days per week they would like to train. Each input will have a loop which will run until correct input is recieved (eg an integer for age.) Error handling will be used to ensure application does not crash at an incorrect input.
All inputs will be assigned to a variable to be called by the final function to print the routine.
#### Age
* Users below 14 will receive a cardio and sports based routine
* Users 14-17 will get a standardised 3 day a week strength routine, they will not have an option to select strength or days
* Users 18+ will then be asked to select strength and days/week
#### Sex
The application will loop until the applicant selects their biological sex M or F. This is used to print the right strength standards table in the next section and has no relevance to the final routine.
#### Strength
The idea is to keep things simple and accessible to a wider audience who may not know their strength levels. A table will be printed to the screen showing the simplest lift, a deadlift. A Deadlift is how much weight you can pick up off the floor until your legs are straight. The table will show bodyweight, deadlift weight, and the resultant strength level from beginner to advanced for the selected sex. User will input a number from 1-3 for their level
#### Days per week
The user will enter a number between 1-7 for how many days per week they would like to train.
After they select the application will run through a loop and if/else statements to select the right routine based on their age, strength 
* < 3 will print a message saying 3 days is minimum for a good routine and they must select again.
* 3 will print a 3 day routine
* 4 will print a 4 day routine
* 5 will print a 5 day routine
* 6 will print a 6 day routine
* 7 will print a message saying 7 days is too much, user needs to rest. Select again
* More than 7 will print an error message allowing user to try again.
* Any other input will print an error message and allow user to try again.

### Workout Routine
The workout routine will be printed in table format showing one weeks worth of training.


## User interaction and experience
The first thing the application will print is a "home page" of sorts containing a large ASCII title and some instructions. 

![](/data/homePage.JPG)

They will recieve clear prompts on what to do next ie "Enter your age". The user will progress through each step of the application by entering the relevant prompts.
At the strength screen a table containing strength standards for the deadlift will be printed. The user will be asked to check how much they can lift and pair it with the strength level. If the user is unsure they can take a guess or select beginner. This will also be explained to the user.

![](/data/strengthStandards.JPG)

Errors will be handled by having each user input wrapped in a loop containing Try/except features. Any errors will be displayed to the user as a printed message and the loop will continue until the application recieves a correct input.

## Control Flow Diagram

![Control Flow Diagram](/data/control_flow_diagram.JPG)