# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import time
import colorama
colorama.init()
from powershell_actions import windows_tweaks_actions

def say_license():
    from login_menu.login_menu import login_input
    return login_input

def windows_tweaks_menu():
    while True:
        pass