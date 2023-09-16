from pyautogui import *
import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
import time
import keyboard
import random
import win32api
import win32con
import time

#defining start clicking function
def start():
    ss = ImageGrab.grab()
    ss_img = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2GRAY)
    start_img =cv2.imread('START.jpg',0)
    result =cv2.matchTemplate(ss_img, start_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    start_x, start_y =max_loc
    h, w =start_img.shape
    cv2.rectangle(ss_img, (start_x,start_y),(start_x+w, start_y+h), (0, 0, 255), 6)
    target_x, target_y = start_x+w/2, start_y +h/2
    pyautogui.moveTo(target_x, target_y, duration=0.5)
    pyautogui.click()
    return [w,int(target_y),target_x]
    
#defining click function 
def click(x,y):
    win32api.SetCursorPos((x,y)) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #clicking mouse down where the cursor is
    time.sleep(0.01)                #0.01 crucial for clicking event
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)   #clicking mouse up where the cursor is


def main():
    w,y, target_x= start()
    x1 = int(target_x-w/2-w/4)  #converting floating points to ints
    x2 = int(target_x-w/8)
    x3 = int(target_x+w/8)
    x4 = int(target_x+w/2+w/4)
    tilesClicked=0


    while (True):
        if keyboard.is_pressed('esc'):
            print(f'no of tiles clicked:{tilesClicked}')
            print('escaping ...')
            break
        if pyautogui.pixel(x1,y)[0] ==0: #checking if pixel value is black
            click(x1,y)                  #clicking tile 1
            print('tile 1 clicked')
            tilesClicked+=1
        if pyautogui.pixel(x2,y)[0] ==0: 
            click(x2,y)                  #clicking tile 2
            print('tile 2 clicked')
            tilesClicked+=1
        if pyautogui.pixel(x3,y)[0] ==0: 
            click(x3,y)                  #clicking tile 3
            print('tile 3 clicked')
            tilesClicked+=1
        if pyautogui.pixel(x4,y)[0] ==0: 
            click(x4,y)                  #clicking tile 4
            print('tile 4 clicked')
            tilesClicked+=1

if __name__ =="__main__":
    main()
