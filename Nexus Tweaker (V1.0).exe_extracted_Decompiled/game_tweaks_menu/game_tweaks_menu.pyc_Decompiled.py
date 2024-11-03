# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import time
import colorama
colorama.init()

def say_license():
    from login_menu.login_menu import login_input
    return login_input

def game_tweaks_menu():
    while True:
        print('\n    \x1b[95m███\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗    \x1b[95m████████\x1b[94m╗\x1b[95m██\x1b[94m╗    \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗ \x1b[95m█████\x1b[94m╗ \x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██████\x1b[94m╗ \n    \x1b[95m████\x1b[94m╗  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝    ╚══\x1b[95m██\x1b[94m╔══╝\x1b[95m██\x1b[94m║    \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║ \x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗   ╚\x1b[95m███\x1b[94m╔╝ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███████\x1b[94m╗       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║ \x1b[95m█\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗  \x1b[95m███████\x1b[94m║\x1b[95m█████\x1b[94m╔╝ \x1b[95m█████\x1b[94m╗  \x1b[95m██████\x1b[94m╔╝\n    \x1b[95m██\x1b[94m║╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝   \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║╚════\x1b[95m██\x1b[94m║       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔═\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m║ ╚\x1b[95m████\x1b[94m║\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╔╝ \x1b[95m██\x1b[94m╗╚\x1b[95m██████\x1b[94m╔╝\x1b[95m███████\x1b[94m║       \x1b[95m██\x1b[94m║   ╚\x1b[95m███\x1b[94m╔\x1b[95m███\x1b[94m╔╝\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\n    \x1b[94m╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
        print('   ', '\x1b[95mDeveloped by \x1b[94mThorstellinii', '                 ', '\x1b[90mVersion: 1.0')
        print('                                          ', '\x1b[92mLast Updated: 21.10.2024')
        print('\x1b[94m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('                                     ', '\x1b[97mLogged in as:\x1b[91m', say_license())
        print()
        print('\x1b[95mGame Tweaks \x1b[94m>')
        print()
        print('\x1b[95m[\x1b[94m1\x1b[95m]\x1b[94m-\x1b[97mFortnite\x1b[0m')
        print('\x1b[95m[\x1b[94m2\x1b[95m]\x1b[94m-\x1b[97mCS2\x1b[0m')
        print()
        print('\x1b[95m[\x1b[94mB\x1b[95m]\x1b[94m-\x1b[97mGo Back')
        print('\x1b[95m[\x1b[94mX\x1b[95m]\x1b[94m-\x1b[97mClose')
        print()
        game_tweaks_input = input('\x1b[95mChoose an Option \x1b[94m>\x1b[97m')
        if game_tweaks_input == 'X' or game_tweaks_input == 'x':
            sys.exit()
        else:
            if game_tweaks_input == 'B' or game_tweaks_input == 'b':
                os.system('cls')
                return
            if game_tweaks_input == '1':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif game_tweaks_input == '2':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            else:
                print('\x1b[91mInvalid option! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')