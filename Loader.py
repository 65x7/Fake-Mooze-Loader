# loader.py
import sys
import time
import os
import random
import string

# Renk desteği
try:
    from colorama import init as colorama_init
    colorama_init()
except Exception:
    pass

RED = "\033[31m"
RESET = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def set_title(title):
    if os.name == "nt":
        os.system(f"title {title}")
    else:
        sys.stdout.write(f"\33]0;{title}\a")
        sys.stdout.flush()

def set_window_size(cols=90, lines=25):
    if os.name == "nt":
        try:
            os.system(f"mode con: cols={cols} lines={lines}")
        except Exception:
            pass

def random_title_suffix(n=32):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(n))

MOOZE_ASCII_FALLBACK = r"""


   888b     d888  .d88888b.   .d88888b. 8888888888P 8888888888 
   8888b   d8888 d88P" "Y88b d88P" "Y88b      d88P  888        
   88888b.d88888 888     888 888     888     d88P   888        
   888Y88888P888 888     888 888     888    d88P    8888888    
   888 Y888P 888 888     888 888     888   d88P     888        
   888  Y8P  888 888     888 888     888  d88P      888        
   888   "   888 Y88b. .d88P Y88b. .d88P d88P       888        
   888       888  "Y88888P"   "Y88888P" d8888888888 8888888888 
                                                            
                                                            
                                                            
"""

def print_mooze_big():
    clear()
    try:
        from pyfiglet import Figlet
        f = Figlet(font='big')
        print(f.renderText("MOOZE"))
    except Exception:
        print(MOOZE_ASCII_FALLBACK)

def main():
    if os.name == "nt":
        set_window_size(90, 25)

    title_suffix = random_title_suffix(32)
    set_title(f"Razer Cortex - {title_suffix}")

    # --- Key ekranı ---
    print_mooze_big()
    print(f"  [ - ] {RED}Key{RESET}:", end=" ")
    try:
        input()  # key ne olursa olsun kabul
    except KeyboardInterrupt:
        print("\nÇıkılıyor...")
        return

    # --- Verifying ---
    set_title(f"Razer Cortex | Verifying Key... - {title_suffix}")
    print_mooze_big()
    print(f"  [ - ] Verifying Your {RED}Key{RESET}")
    time.sleep(1.8)

    # --- Validated ---
    set_title(f"Razer Cortex | Key Validated - {title_suffix}")
    print_mooze_big()
    print(f"  [ - ] {RED}Validated{RESET} Your {RED}Key{RESET}")
    time.sleep(1.5)

    # --- Injecting ---
    set_title(f"Razer Cortex | Injecting... - {title_suffix}")
    for sec in range(5, -1, -1):
        print_mooze_big()
        print(f"  [ - ] Injected Hiding Tray in {RED}{sec}{RESET} seconds")
        if sec > 0:
            time.sleep(1)
            clear()

    time.sleep(0.8)
    print_mooze_big()
    print(f"  [ - ] Injected Hiding Tray in {RED}0{RESET} seconds")
    time.sleep(0.8)
    set_title(f"Razer Cortex | Done - {title_suffix}")
    print("  [ - ] Closing...")
    time.sleep(1)
    clear()
    set_title("")

if __name__ == "__main__":
    main()
