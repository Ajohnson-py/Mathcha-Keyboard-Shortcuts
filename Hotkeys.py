import pyautogui
import time

from pynput.keyboard import *
from pynput.mouse import Button, Controller


hotkeys = [
    {Key.ctrl, KeyCode(char='u')},
    {Key.ctrl, KeyCode(char='v')},
    {Key.ctrl, KeyCode(char='i')},
    {Key.ctrl, KeyCode(char='j')},
    {Key.ctrl, KeyCode(char='F')},
    {Key.ctrl, KeyCode(char='k')},
    {Key.ctrl, KeyCode(char='r')},
]

keys_pressed = set()


def execute(key):
    #print(key)
    #print(get_mathcha_custom_button_location())
    pyautogui.keyDown('\\')
    time.sleep(0.3)
    pyautogui.keyUp('\\')
    button_location = get_mathcha_custom_button_location()
    pyautogui.click(button_location)

    if key == 'i':
        pyautogui.write('i')
        pyautogui.press('enter')


def on_press(key):
    if any([key in combo for combo in hotkeys]):
        keys_pressed.add(key)
        if any(all(k in keys_pressed for k in combo) for combo in hotkeys):
            execute(key)


def off_press(key):
    if any([key in combo for combo in hotkeys]):
        print(keys_pressed)
        keys_pressed.remove(key)


def get_mathcha_custom_button_location():
    return pyautogui.locateCenterOnScreen('Mathcha_button.png')


with Listener(on_press=on_press, on_release=off_press) as listener:
    listener.join()
