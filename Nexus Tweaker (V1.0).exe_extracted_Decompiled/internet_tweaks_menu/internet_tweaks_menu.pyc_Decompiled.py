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

def internet_tweaks_menu():
    while True:
        print('\n    \x1b[95m███\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗    \x1b[95m████████\x1b[94m╗\x1b[95m██\x1b[94m╗    \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗ \x1b[95m█████\x1b[94m╗ \x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██████\x1b[94m╗ \n    \x1b[95m████\x1b[94m╗  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝    ╚══\x1b[95m██\x1b[94m╔══╝\x1b[95m██\x1b[94m║    \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║ \x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗   ╚\x1b[95m███\x1b[94m╔╝ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███████\x1b[94m╗       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║ \x1b[95m█\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗  \x1b[95m███████\x1b[94m║\x1b[95m█████\x1b[94m╔╝ \x1b[95m█████\x1b[94m╗  \x1b[95m██████\x1b[94m╔╝\n    \x1b[95m██\x1b[94m║╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝   \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║╚════\x1b[95m██\x1b[94m║       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔═\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m║ ╚\x1b[95m████\x1b[94m║\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╔╝ \x1b[95m██\x1b[94m╗╚\x1b[95m██████\x1b[94m╔╝\x1b[95m███████\x1b[94m║       \x1b[95m██\x1b[94m║   ╚\x1b[95m███\x1b[94m╔\x1b[95m███\x1b[94m╔╝\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\n    \x1b[94m╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
        print('   ', '\x1b[95mDeveloped by \x1b[94mThorstellinii', '                 ', '\x1b[90mVersion: 1.0')
        print('                                          ', '\x1b[92mLast Updated: 21.10.2024')
        print('\x1b[94m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('                                     ', '\x1b[97mLogged in as:\x1b[91m', say_license())
        print()
        print('\x1b[95mInternet Tweaks \x1b[94m>')
        print()
        print('\x1b[95m[\x1b[94m1\x1b[95m]\x1b[94m-\x1b[97mRefresh Internet')
        print('\x1b[95m[\x1b[94m2\x1b[95m]\x1b[94m-\x1b[97mClear DNS Cache')
        print('\x1b[95m[\x1b[94m3\x1b[95m]\x1b[94m-\x1b[97mUse Best DNS Server')
        print('\x1b[95m[\x1b[94m4\x1b[95m]\x1b[94m-\x1b[97mAdvanced Nexus Network Tweaks')
        print()
        print('\x1b[95m[\x1b[94mA\x1b[95m]\x1b[94m-\x1b[97mAll')
        print()
        print('\x1b[95m[\x1b[94mB\x1b[95m]\x1b[94m-\x1b[97mGo Back')
        print('\x1b[95m[\x1b[94mX\x1b[95m]\x1b[94m-\x1b[97mClose')
        print()
        internet_tweaks_input = input('\x1b[95mChoose an Option \x1b[94m>\x1b[97m')
        if internet_tweaks_input == 'X' or internet_tweaks_input == 'x':
            sys.exit()
        else:
            if internet_tweaks_input == 'B' or internet_tweaks_input == 'b':
                os.system('cls')
                return
            if internet_tweaks_input == 'A' or internet_tweaks_input == 'a':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif internet_tweaks_input == '1':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif internet_tweaks_input == '2':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif internet_tweaks_input == '3':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif internet_tweaks_input == '4':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            else:
                print('\x1b[91mInvalid option! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')