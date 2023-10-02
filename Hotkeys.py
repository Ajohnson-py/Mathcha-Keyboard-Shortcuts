import time
from pynput.keyboard import Controller, Listener, Key, KeyCode


text_start = False
text_end = False
bold = False
vector = False
function = False

hotkeys = [
    {Key.ctrl, KeyCode(char='b')},
    {Key.ctrl, KeyCode(char='v')},
    {Key.ctrl, KeyCode(char='m')},
    {Key.ctrl, KeyCode(char='f')}
]

keys_pressed = set()
keyboard = Controller()

# accesses the mathbf command
def mathbf(text):
    command = "mathbf"
    # highlights text
    keyboard.press(Key.shift)
    if len(text) == 0:
        for i in range(len(text) + 1):
            keyboard.press(Key.left)
    else:
        for i in range(len(text)):
            keyboard.press(Key.left)
    keyboard.release(Key.shift)

    # types command
    time.sleep(0.2)
    keyboard.press('\\')
    time.sleep(0.2)
    for letter in command:
        keyboard.press(letter)
    keyboard.press(Key.enter)

    # makes text no longer highlighted
    time.sleep(0.2) 
    keyboard.press(Key.shift)
    if len(text) == 0:
        for i in range(len(text) + 1):
            keyboard.press(Key.right)
    else:
        for i in range(len(text)):
            keyboard.press(Key.right)
    keyboard.release(Key.shift)
    keys_pressed.discard(text)

# accesses the vec command
def vec(text):
    command = "vec"

    # highlights text
    keyboard.press(Key.shift)
    if len(text) == 0:
        for i in range(len(text) + 1):
            keyboard.press(Key.left)
    else:
        for i in range(len(text)):
            keyboard.press(Key.left)
    keyboard.release(Key.shift)

    # types command
    time.sleep(0.2)
    keyboard.press('\\')
    time.sleep(0.2)
    for letter in command:
        keyboard.press(letter)
    keyboard.press(Key.enter)

    # makes text no longer highlighted
    time.sleep(0.2) 
    keyboard.press(Key.shift)
    if len(text) == 0:
        for i in range(len(text) + 1):
            keyboard.press(Key.right)
    else:
        for i in range(len(text)):
            keyboard.press(Key.right)
    keyboard.release(Key.shift)
    keys_pressed.discard(text)

# makes a vmatrix and writes i, j and k on top row
def cross_product():
    command = "vmatrix"

    # gets matrix
    keyboard.press('\\')
    time.sleep(0.2) 
    for letter in command:
        keyboard.press(letter)
    keyboard.press(Key.enter)

    #formats matrix
    keyboard.press(Key.enter)
    time.sleep(0.2) 
    keyboard.press(Key.right)
    time.sleep(0.2) 
    keyboard.press(Key.enter)
    time.sleep(0.2) 
    keyboard.press(Key.enter)
    time.sleep(0.2) 
    keyboard.press(Key.enter)

    # fills in i, j, and k
    # j
    time.sleep(0.1)
    keyboard.press(Key.up)
    keyboard.press(KeyCode(char='j'))
    j = set()
    j.add(KeyCode(char='j'))
    mathbf(j)
    # i
    time.sleep(0.1)
    keyboard.press(Key.left)
    keyboard.press(Key.left)
    keyboard.press(KeyCode(char='i'))
    i = set()
    i.add(KeyCode(char='i'))
    mathbf(i)
    # k
    time.sleep(0.1)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(Key.right)
    keyboard.press(KeyCode(char='k'))
    k = set()
    k.add(KeyCode(char='k'))
    mathbf(k)

#makes a function f with the specified number of variables
def f(text):
    keyboard.press(Key.backspace)
    keyboard.press(KeyCode(char='f'))
    keyboard.press(KeyCode(char='('))
    print(text)

    if any([key == KeyCode(char='1') for key in text]):
        keyboard.press(KeyCode(char='x'))
        keyboard.press(KeyCode(char=')'))
        keyboard.press(KeyCode(char='='))
    elif any([key == KeyCode(char='2') for key in text]):
        keyboard.press(KeyCode(char='x'))
        keyboard.press(KeyCode(char=','))
        keyboard.press(KeyCode(char='y'))
        keyboard.press(KeyCode(char=')'))
        keyboard.press(KeyCode(char='='))
    elif any([key == KeyCode(char='3') for key in text]):
        keyboard.press(KeyCode(char='x'))
        keyboard.press(KeyCode(char=','))
        keyboard.press(KeyCode(char='y'))
        keyboard.press(KeyCode(char=','))
        keyboard.press(KeyCode(char='z'))
        keyboard.press(KeyCode(char=')'))
        keyboard.press(KeyCode(char='='))

def get_text():
    for combo in keys_pressed.copy():
        if combo == Key.shift or combo == Key.shift_r or combo == Key.enter:
                keys_pressed.discard(combo)

    return keys_pressed

def execute(key):
    global text_start
    global text_end
    global bold
    global vector
    global function

    if text_start == True:
        for combo in keys_pressed:
            if combo == Key.enter:
                text_end = True
                break

        if text_end == True:
            text = get_text()
            keyboard.press(Key.backspace)
            time.sleep(0.1)
            if bold == True:
                mathbf(text)
            elif vector == True:
                vec(text)
            else:
                f(text)
            text_end = False
            text_start = False
            bold = False
            vector = False
            function = False
            keys_pressed.clear() # here because of bug when using a hotkey multiple times. Find better fix

    if key == KeyCode(char='b') or key == KeyCode(char='v') or key == KeyCode(char='f'):
        text_start = True
        if key == KeyCode(char='b'):
            bold = True
        elif key == KeyCode(char='v'):
            vector = True
        else:
            function = True
    
    if key == KeyCode(char='m'):
        cross_product()
                

def on_press(key):
    if text_start == True:
        keys_pressed.add(key)
        execute(key)

    if any([key in combo for combo in hotkeys]):
        keys_pressed.add(key)
        if any(all(k in keys_pressed for k in combo) for combo in hotkeys):
            execute(key)

def off_press(key):
    if text_start == True:
        pass

    if any([key in combo for combo in hotkeys]):
        keys_pressed.discard(key)


with Listener(on_press=on_press, on_release=off_press) as listener:
    listener.join()
