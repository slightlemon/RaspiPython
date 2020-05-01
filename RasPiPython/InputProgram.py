import time
import keyboard
from evdev import UInput, ecodes as e
def setup():
    global command
def InputUp():
    keyboard.press_and_release('up')
def InputDown():
    keyboard.press_and_release('down')
def InputLeft():
    keyboard.press_and_release('left')
def InputRight():
    keyboard.press_and_release('right')
def InputA():
    keyboard.press_and_release('a')
def InputB():
    keyboard.press_and_release('b')
def InputC():
    keyboard.press_and_release('F1')
def InputD():
    keyboard.press_and_release('esc')
def close():
    command.stop()
if __name__=='__main__':
    setup()
