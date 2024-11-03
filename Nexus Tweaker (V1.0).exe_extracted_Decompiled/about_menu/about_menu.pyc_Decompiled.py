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

def about_menu():
    while True:
        print('\n    \x1b[95m███\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗    \x1b[95m████████\x1b[94m╗\x1b[95m██\x1b[94m╗    \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗ \x1b[95m█████\x1b[94m╗ \x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██████\x1b[94m╗ \n    \x1b[95m████\x1b[94m╗  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝    ╚══\x1b[95m██\x1b[94m╔══╝\x1b[95m██\x1b[94m║    \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║ \x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗   ╚\x1b[95m███\x1b[94m╔╝ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███████\x1b[94m╗       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║ \x1b[95m█\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗  \x1b[95m███████\x1b[94m║\x1b[95m█████\x1b[94m╔╝ \x1b[95m█████\x1b[94m╗  \x1b[95m██████\x1b[94m╔╝\n    \x1b[95m██\x1b[94m║╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝   \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║╚════\x1b[95m██\x1b[94m║       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔═\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m║ ╚\x1b[95m████\x1b[94m║\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╔╝ \x1b[95m██\x1b[94m╗╚\x1b[95m██████\x1b[94m╔╝\x1b[95m███████\x1b[94m║       \x1b[95m██\x1b[94m║   ╚\x1b[95m███\x1b[94m╔\x1b[95m███\x1b[94m╔╝\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\n    \x1b[94m╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
        print('   ', '\x1b[95mDeveloped by \x1b[94mThorstellinii', '                 ', '\x1b[90mVersion: 1.0')
        print('                                          ', '\x1b[92mLast Updated: 21.10.2024')
        print('\x1b[94m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('                                     ', '\x1b[97mLogged in as:\x1b[91m', say_license())
        print()
        print('\x1b[95mAbout \x1b[94m>')
        print()
        print()
        print('                  ', '\x1b[92mThe Nexus Tweaker is developed to maximize the performance of PCs.')
        print()
        print()
        print('\x1b[95mYour License:\x1b[91m', say_license(), '\x1b[94m(Free License)')
        print('\x1b[95mDeveloped by \x1b[94mThorstellinii')
        print('\x1b[95mCurrent Version:\x1b[94m 1.0')
        print('\x1b[95mLast Updated: \x1b[94m21.10.2024')
        print()
        print('\x1b[95m[\x1b[94mB\x1b[95m]\x1b[94m-\x1b[97mGo Back')
        print('\x1b[95m[\x1b[94mX\x1b[95m]\x1b[94m-\x1b[97mClose')
        print()
        about_menu_input = input('\x1b[95mChoose an Option \x1b[94m>\x1b[97m')
        if about_menu_input == 'X' or about_menu_input == 'x':
            sys.exit()
        else:
            if about_menu_input == 'B' or about_menu_input == 'b':
                os.system('cls')
                return
            print('\x1b[91mInvalid option! (Wait 2 seconds)')
            time.sleep(2)
            os.system('cls')