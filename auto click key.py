from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
keyboard.press('z')
keyboard.release('z')
