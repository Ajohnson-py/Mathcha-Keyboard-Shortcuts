import time
from pynput.keyboard import Key, Controller

keyboard = Controller()


def type_command(command):
    keyboard.press('\\')
    time.sleep(0.1)
    for char in command:
        keyboard.press(char)
    keyboard.press(Key.enter)


def select_text(length):
    keyboard.press(Key.shift)
    for _ in range(length):
        keyboard.press(Key.left)
    keyboard.release(Key.shift)


def unselect_text(length):
    keyboard.press(Key.shift)
    for _ in range(length):
        keyboard.press(Key.right)
    keyboard.release(Key.shift)


def mathbf(text):
    # Offset enter key being pressed
    keyboard.press(Key.backspace)

    # Select the text
    select_text(len(text))
    time.sleep(0.1)

    # Insert \mathbf command
    type_command("mathbf")
    keyboard.press(Key.enter)
    time.sleep(0.15)

    # Unselect the text
    unselect_text(len(text))


def vec(text):
    # Offset enter key being pressed
    keyboard.press(Key.backspace)

    # Select captured text
    select_text(len(text))
    time.sleep(0.15)

    # Insert \vec command
    type_command("vec")

    # Move back to end of text
    for _ in range(len(text) + 1):
        keyboard.press(Key.right)


def cross_product():
    # Insert \vmatrix command
    type_command("vmatrix")

    # Create another row
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.press(Key.enter)

    # Create another column
    time.sleep(0.2)
    keyboard.press(Key.enter)
    time.sleep(0.2)
    keyboard.press(Key.right)
    time.sleep(0.2)
    keyboard.press(Key.enter)

    # Fill in i, j, k for the top row

    # j
    time.sleep(0.2)
    keyboard.press(Key.up)
    keyboard.press('j')
    time.sleep(0.2)
    select_text(1)
    time.sleep(0.2)
    type_command("mathbf")
    time.sleep(0.2)
    keyboard.press(Key.left)

    # i
    time.sleep(0.2)
    keyboard.press('i')
    time.sleep(0.2)
    select_text(1)
    time.sleep(0.2)
    type_command("mathbf")
    time.sleep(0.2)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.right)

    # k
    time.sleep(0.2)
    keyboard.press('k')
    select_text(1)
    time.sleep(0.2)
    type_command("mathbf")
    time.sleep(0.2)
    keyboard.press(Key.right)


def function(text):
    # Offset enter key being pressed
    keyboard.press(Key.backspace)

    # Delete captured text
    for _ in range(len(text)):
        keyboard.press(Key.backspace)

    # Check captured text to determine function notation
    keyboard.press('f')

    # checks if partial derivative is wanted
    for axis in ['x', 'y', 'z']:
        if any(key == axis for key in text):
            keyboard.press('_')
            keyboard.press(axis)
            break

    keyboard.press('(')

    # Check for dimensions and press corresponding keys
    dimensions = {
        '1': ['x'],
        '2': ['x', ',', 'y'],
        '3': ['x', ',', 'y', ',', 'z'],
    }
    for dim, keys in dimensions.items():
        if any(key == dim for key in text):
            for char in keys:
                keyboard.press(char)
            break

    keyboard.press(')')
    keyboard.press('=')


def integral():
    type_command("int")


def oint():
    type_command("oint")
