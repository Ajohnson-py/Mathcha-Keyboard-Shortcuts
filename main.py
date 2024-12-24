from pynput.keyboard import Listener, Key
from hotkeys import HotkeyManager
from commands import mathbf, vec, cross_product, function, integral, oint

hotkey_manager = HotkeyManager()
active_text = []  # Buffer for user input layered hotkey modes
layered_hotkey = ""  # Track if the bold, vector, or function mode is active


def execute_action(action, key):
    global layered_hotkey, active_text

    # Call layered hotkeys when text is captured
    if not layered_hotkey == "" and key == Key.enter:
        # Apply formatting to the captured text
        if layered_hotkey == "bold":
            mathbf("".join(active_text))
            active_text.clear()
        elif layered_hotkey == "vector":
            vec("".join(active_text))
            active_text.clear()
        elif layered_hotkey == "function":
            function("".join(active_text))
            active_text.clear()
        layered_hotkey = ""
    elif hasattr(key, 'char') and key.char:  # Record alphanumeric characters
        active_text.append(key.char)

    if action == "bold":
        layered_hotkey = "bold"
        active_text.clear()  # Reset the buffer when entering layered hotkey mode
    elif action == "vector":
        layered_hotkey = "vector"
        active_text.clear()  # Reset the buffer when entering layered hotkey mode
    elif action == "function":
        layered_hotkey = "function"
        active_text.clear()  # Reset the buffer when entering layered hotkey mode
    elif action == "cross_product":
        cross_product()
    elif action == "integral":
        integral()
    elif action == "oint":
        oint()


def on_press(key):
    global layered_hotkey

    hotkey_manager.add_key(key)
    action = hotkey_manager.get_action()

    if action or not layered_hotkey == "":
        execute_action(action, key)


def on_release(key):
    hotkey_manager.remove_key(key)


if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
