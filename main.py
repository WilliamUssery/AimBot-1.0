from pyautogui import * 
import pyautogui
import time 
import keyboard
import random
import win32api, win32con

# Make sure to add an exception handle for this like this. The only way that I was
# able to make his version work was to 
"""

while 1:
    if pyautogui.locateOnScreen('stickman.png', confidence=0.7) != None:
        print("I can see him!")
        time.sleep(0.5)
    else:
        print("I can't see that slippery fool")
        time.sleep(0.5)

    """

# The way that I did it I had to make it a BOOLEAN with the "try:" and "exception:" statement
while True:
    try:
        if pyautogui.locateOnScreen('stickman.png', confidence=0.7) != None:
            print("I can see him!")
            time.sleep(0.5)
        else:
            print("I can't see that slippery fool")
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException:
        print("Image not found error caught")
    time.sleep(1.5)