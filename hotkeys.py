from pynput.keyboard import Key, KeyCode


class HotkeyManager:
    def __init__(self):
        self.hotkeys = {
            frozenset([Key.ctrl, KeyCode(char='b')]): "bold",
            frozenset([Key.ctrl, KeyCode(char='v')]): "vector",
            frozenset([Key.ctrl, KeyCode(char='m')]): "cross_product",
            frozenset([Key.ctrl, KeyCode(char='f')]): "function",
            frozenset([Key.ctrl, KeyCode(char='i')]): "integral",
            frozenset([Key.ctrl, KeyCode(char='o')]): "oint",
        }
        self.keys_pressed = set()
        self.last_combo = None  # Keeps track of the last executed hotkey.

    def add_key(self, key):
        self.keys_pressed.add(key)

    def remove_key(self, key):
        self.keys_pressed.discard(key)
        # Reset last_combo if all keys in the combo are released
        if self.last_combo and not self.last_combo.intersection(self.keys_pressed):
            self.last_combo = None

    def get_action(self):
        for combo, action in self.hotkeys.items():
            if combo.issubset(self.keys_pressed) and combo != self.last_combo:
                self.last_combo = combo
                return action
        return None

