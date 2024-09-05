import threading
from pynput import keyboard, mouse
import time
import sys

mouse_controller = mouse.Controller()
clicking = False
terminate_program = False  # Flag to terminate the program


# Handle key presses to toggle clicking on/off
def on_press(key):
    global clicking, terminate_program
    try:
        if key.char == 's':
            clicking = True
            print("Auto-clicking started.")
        elif key.char == 'e':
            clicking = False
            print("Auto-clicking stopped.")
    except AttributeError:
        if key == keyboard.Key.esc:
            terminate_program = True  # Set flag to terminate the program
            print("Exiting program...")
            return False  # Stop the listener


# Function for automatic clicking
def auto_clicker():
    global terminate_program
    while not terminate_program:
        # Only click if 'clicking' is set to True
        if clicking:
            mouse_controller.click(mouse.Button.left, 1)  # Corrected click method
            time.sleep(0.01)  # Sleep for a short amount of time between clicks
        else:
            time.sleep(0.1)  # Sleep longer when not clicking to reduce CPU usage

    sys.exit()  # Exit the program when 'terminate_program' is True


# Listener for keyboard input
def listen_for_keys():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# Run the key listener in a separate thread
key_listener_thread = threading.Thread(target=listen_for_keys)
key_listener_thread.daemon = True
key_listener_thread.start()

# Start the auto clicker in the main thread
auto_clicker()