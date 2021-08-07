import random
import time

def Dice():
    min = 1
    max = 6
    dice = random.randint(min, max)
    print(f"Your values are {dice}")

Dice()
print("Do you wanna play again?")
user_action = input()
user_action = "yes"

while user_action != "Yes" or user_action != "y" or user_action != "yes":
    Dice()
    time.sleep(1)
    user_action = input("again?:\t")
else:
    print("You ended it!")
