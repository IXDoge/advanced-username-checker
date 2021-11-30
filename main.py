# Project requested at https://ixdoge.com/request/

import random, string, requests
from colorama import Fore, Style
from time import sleep

s = requests.session() # Makes the tool way faster

def write_file(arg: str) -> None: # Writes available usernames to users.txt
    with open("users.txt", "a", encoding = "UTF-8") as f:
        f.write(f"{arg}\n")

def start():
    print("""
Modes:
[1]: Letters + Digits
[2]: Letters only
[3]: Digits only
    """)
    mode = int(input("Select mode: ")) # Asks the mode you want to use
    if mode == 1: # Checks if the selected mode is 1
        mode = string.ascii_letters + string.digits # Sets the mode to letters & digits
        print(f"Selected mode: Letters & Digits")
    elif mode == 2:
        mode = string.ascii_letters
        print(f"Selected mode: Letters")
    elif mode == 3:
        mode = string.digits
        print(f"Selected mode: Digits")
    letters = int(input("Amount of letters: ")) # Asks for the amount of letters you want to be in a username
    print(f"Amount of letters set to: {letters}")
    while True:
        code = ('').join(random.choices(mode, k=letters)) # Sets the mode and amount of letters
        r = s.get(f"https://github.com/{code}")
        if r.status_code == 200:
            print(f"{Style.BRIGHT}{Fore.RED}[UNAVAILABLE] > github.com/{code}{Fore.RESET}")
        elif r.status_code == 429:
            print("2 many requests")
            sleep(30)
        else:
            write_file(code)
            print(f"{Fore.GREEN}[AVAILABLE] github.com/{Fore.MAGENTA}{code}")

print("""
[1]: No proxy mode
""")
selection = input('>>> ')
selections = [start]
selections[int(selection) -1]()
