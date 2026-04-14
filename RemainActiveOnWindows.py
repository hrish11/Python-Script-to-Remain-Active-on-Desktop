import pyautogui
import time
import keyboard
import sys

pyautogui.FAILSAFE = False
    
try:
    while True:
        if keyboard.is_pressed('esc'):
            print("ESC pressed, exiting...")
            sys.exit() 
        time.sleep(15)

        for i in range(0, 100):
            if keyboard.is_pressed('esc'):
                print("ESC pressed, exiting...")
                sys.exit()   
            pyautogui.moveTo(0, i * 5)

        for i in range(0, 3):
            if keyboard.is_pressed('esc'):
                print("ESC pressed, exiting...")
                sys.exit()  
            pyautogui.press('shift')

except Exception as e:
    print(f"An error occurred: {e}")
