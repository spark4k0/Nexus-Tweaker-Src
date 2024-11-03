# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import subprocess
import os
import sys
import time
import colorama
colorama.init()

def restart_computer():
    restart_computer_input = input('\x1b[94mDo you want to restart your computer to save the changes? Y/N >')
    if restart_computer_input == 'Y' or restart_computer_input == 'y':
        subprocess.run(['powershell', '-Command', 'Restart-Computer'])
    else:
        print('\x1b[91mProcess aborted! (wait 2 seconds)')
        time.sleep(2)