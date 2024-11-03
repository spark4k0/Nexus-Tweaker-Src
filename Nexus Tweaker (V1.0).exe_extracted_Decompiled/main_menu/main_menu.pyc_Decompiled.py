# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import time
import colorama
colorama.init()
from about_menu import about_menu
from extras_menu import extras_menu
from windows_tweaks_menu import windows_tweaks_menu
from hardware_tweaks_menu import hardware_tweaks_menu
from internet_tweaks_menu import internet_tweaks_menu
from game_tweaks_menu import game_tweaks_menu
from debloater_menu import debloater_menu
from powershell_actions import restart_computer_action

def say_license():
    from login_menu.login_menu import login_input
    return login_input

def main_menu():
    while True:
        pass