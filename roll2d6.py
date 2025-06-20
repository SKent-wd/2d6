import datetime
import numpy as np
from numpy import random
import sys
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

# Global variables
makeRoll = True  # Flag for allowing the dice roll
rollCount = 0  # Count the number of dice rolls
rollMessage = "Now make your move."  # Default message


# Function simulates rolling 2 6-sided dice, displaying the result and a message
def roll_the_dice():
    global makeRoll
    global rollCount
    global rollMessage

    if rollCount < 3:
        # Below code uses NumPy to get 2 random numbers, each between 1 and 6
        roll = random.randint(1, 7, size=2)
        d6_1 = int(roll[0])  # Dice 1
        d6_2 = int(roll[1])  # Dice 2

        rollCount += 1  # Increment the dice roll count

        rolled_total = d6_1 + d6_2  # Add the dice roll results together

        rollMessage = decide_message(rolled_total)  # Set message

        # Begin displaying output
        print("Rolling 2 6-sided dice gives... ")
        print(str(d6_1) + " and " + str(d6_2) + ", making " + str(rolled_total) + ".")
        print(rollMessage)

        record_roll(d6_1, d6_2)  # Log the rolled numbers
        plot_roll(d6_1, d6_2)  # Plot the rolled numbers

        # Stop rolling if the result is not 2 sixes
        if rolled_total != 12:
            makeRoll = False
    else:
        makeRoll = False # Stops rolls when maximum roll count reached
        print("...or not. I think you've had enough turns...!")


# Function sets the output message based on the numerical value given
def decide_message(rolled_total=0):
    global rollMessage
    global rollCount

    # Catch and stop the process if results are out of range
    if rolled_total < 2 or rolled_total > 12:
        sys.exit("Total returned as " + str(rolled_total) + " - totals can only be from 2 to 12.")

    # If this is a bonus roll, reset the default message
    if rollCount > 1:
        rollMessage = "Now make your next move."  # Default bonus roll message

    # Set an output message based on the total value rolled
    if rolled_total == 2:
        rollMessage = "Snake eyes!"
    elif rolled_total == 3:
        rollMessage = "Cup of tea!"
    elif rolled_total == 4:
        rollMessage = "Key in the door!"
    elif rolled_total == 5:
        rollMessage = "Man alive!"
    elif rolled_total == 6:
        rollMessage = "Halfway there!"
    elif rolled_total == 7:
        rollMessage = "Lucky for some!"
    elif rolled_total == 8:
        rollMessage = "Garden gate!"
    elif rolled_total == 11:
        rollMessage = "Almost there!"
    elif rolled_total == 12:
        rollMessage = "Roll again!"
    return rollMessage


# Writes the results into a text file
def record_roll(d6_1=0, d6_2=0):
    rolled_total = d6_1 + d6_2  # Added the dice rolls together
    now_val = datetime.datetime.now() # Get the current datetime
    now_string = now_val.strftime("%Y%m%d") # Get string representing current date
    now_txt = now_val.strftime("%Y-%m-%d %H:%M:%S") # Get string representing current date and time
    f = open("roll_logs/roll_log_" + now_string + ".txt", "a") # Opens (creates if required) text log for current date
    f.write(now_txt + " - " + str(d6_1) + " + " + str(d6_2) + " = " + str(rolled_total) + "\n")
    f.close()


# Creates a plot and saves image based on
def plot_roll(d6_1=0, d6_2=0):
    make_plot = input("Create plot based on roll (y/n)?")  # Ask user to confirm plot creation
    if make_plot == "Y" or make_plot == "y":
        rolled_total = d6_1 + d6_2  # Added the dice rolls together
        now_val = datetime.datetime.now()  # Get the current datetime
        now_string = now_val.strftime("%Y%m%d%H%M%S")  # Create string representing current datetime

        x = np.array(["Die 1", "Die 2", "Total"])  # X axis labels
        y = np.array([d6_1, d6_2, rolled_total])  # Y axis values

        plt.bar(x, y)
        plt.savefig("roll_plots/roll_plot_" + now_string + ".png")  # Save the plot as a png file

        print("roll_plot_" + now_string + ".png has been created.")
    elif make_plot == "N" or make_plot == "n":
        pass  # Do nothing and continue process
    else:
        print("Please type either Y or N.")  # Remind user of valid options


# Prompts user to start the dice roll
while makeRoll:
    startRoll = input("Roll the dice (y/n)?")  # Ask user to confirm dice roll

    if startRoll == "Y" or startRoll == "y":
        roll_the_dice()  # User has agreed to roll the dice
    elif startRoll == "N" or startRoll == "n":
        print("Oh, okay then.")  # No dice roll, stop process
        break
    else:
        print("Um, that's not a Y or an N?")  # Remind user of valid options
