# **AIMBOT 1.0**
---
### This is mostly for personal practice for me. If you want to replicate this please do! For the time (2025/04/15). 
### The links that I will be working with are [Youtube-Kain Brose-(How to make advanced image recognition bots using python)](https://www.youtube.com/watch?v=YRAIUA-Oc1Y). Feel free to go watch hit videos. He is very to the point with his videos.
### This code is only writen in Python.

## Libraries
```python
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python
```

## Imports for the video
```python
from pyautogui import * 
import pyautogui
import time 
import keyboard
import random
import win32api, win32con
```
## First Part of the video "Piano_Tiles.py" 
Here is the link he used [Piano-Tiles-link](https://www.agame.com/game/magic-piano-tiles). 
![Display-RGB-Code](Images\Piano_Tiles_Running_Code.png)

I like to treat this as my print("Hello World") to see if I am on the right track. Now we will start programing a bot to play this game.

We are now going to make parameters for the bot. You will need the (x,y) coordinates of each TILE. There should be 4 things that you need. Example in "Piano_Tiles.py"

Go the py file and look at it and follow the video! 

