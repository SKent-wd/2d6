import random
import datetime

#Global variables
makeRoll = True #Flag for allowing the dice roll
rollCount = 0 #Count the number of dice rolls
rollMessage = "Now make your move." #Default message

#Function simulates rolling 2 6-sided dice, displaying the result and a message
def roll_the_dice():
    global makeRoll
    global rollCount
    global rollMessage

    if rollCount < 3:
        d6_1 = int(random.randrange(1, 7)) #Dice 1
        d6_2 = int(random.randrange(1, 7)) #Dice 2

        #Below code can be used with NumPy - to be implemented later
        #roll = random.randint(1, 7, size=(2))
        #d6_1 = roll[0]
        #d6_2 = roll[1]

        rollCount += 1 #Increment the dice roll count

        rolled_total = d6_1 + d6_2 #Add the dice roll results together

        rollMessage = decide_message(rolled_total) #Set message

        print("Rolling 2 6-sided dice gives... ")
        print(str(d6_1) + " and " + str(d6_2) + ", making " + str(rolled_total) + ".")
        print(rollMessage)

        record_roll(d6_1, d6_2) #Log the rolled numbers

        #Stop rolling if the result is not 2 sixes
        if rolled_total != 12:
            makeRoll = False
    else:
        makeRoll = False
        print("...or not. I think you've had enough turns...!")

#Function sets the output message based on the numerical value given
def decide_message(rolled_total = 0):
    global rollMessage
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
    elif rolled_total == 11:
        rollMessage = "Almost there!"
    elif rolled_total == 12:
        rollMessage = "Roll again!"
    return rollMessage

#Writes the results into a text file
def record_roll(d6_1 = 0, d6_2 = 0):
    rolled_total = d6_1 + d6_2 #Added the dice rolls together
    now_val = datetime.datetime.now()
    now_string = now_val.strftime("%Y%m%d")
    now_txt = now_val.strftime("%Y-%m-%d %H:%M:%S")
    f = open("roll_logs/roll_log_" + now_string + ".txt", "a")
    f.write(now_txt + " - " + str(d6_1) + " + " + str(d6_2) + " = " + str(rolled_total) + "\n")
    f.close()

#Prompts user to start the dice roll
while makeRoll:
    startRoll = input("Roll the dice (y/n)?") #Ask user to confirm dice roll

    if startRoll == "Y" or startRoll == "y":
        roll_the_dice() #User has agreed to roll the dice
    elif startRoll == "N" or startRoll == "n":
        print("Oh, okay then.") #No dice roll, stop process
        break
    else:
        print("Um, that's not a Y or an N?") #Remind user of valid options