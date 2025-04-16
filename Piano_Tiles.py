from pyautogui import * 
import pyautogui
import time 
import keyboard
import random
import win32api, win32con

# pyautogui.displayMousePosition() # Uncomment this to run this.
# *Note* This is set up for my screen. You will have to CHANGE IT for yourself
# TILE 1: (1500, 550)|
# TILE 2: (1630, 550)|
# TILE 3: (1745, 550)|
# TILE 4: (1860, 550)|

# Note that the way that RGB values work is that when
# they eluminate light, the value of WHITE will be MAX (254,254,254). 
# When the value of BLACK means that there isnt anything being show, 
# so the value will be (0,0,0)

# We know that our goal of this program is to click the BLACK TILES *(0,0,0)*

# Here is the Win32API He uses. This will click (x,y) position.
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Here is a BOOLEAN that runs when until the 'q' key is pressed
while keyboard.is_pressed('q') == False: # This is the EXIT
    if pyautogui.pixel(1500, 550)[0] == 0: # These are the TILE Positions you might need to change.
        click(1500, 550)
    if pyautogui.pixel(1630, 550)[0] == 0:
        click(1630, 550)
    if pyautogui.pixel(1745, 550)[0] == 0:
        click(1745, 550)
    if pyautogui.pixel(1860, 550)[0] == 0:
        click(1860, 550)

