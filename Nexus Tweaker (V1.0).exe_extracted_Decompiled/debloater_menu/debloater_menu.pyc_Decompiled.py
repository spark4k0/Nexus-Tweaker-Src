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

def debloater():
    while True:
        print('\n    \x1b[95m███\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗    \x1b[95m████████\x1b[94m╗\x1b[95m██\x1b[94m╗    \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗ \x1b[95m█████\x1b[94m╗ \x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██████\x1b[94m╗ \n    \x1b[95m████\x1b[94m╗  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝    ╚══\x1b[95m██\x1b[94m╔══╝\x1b[95m██\x1b[94m║    \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║ \x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗   ╚\x1b[95m███\x1b[94m╔╝ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███████\x1b[94m╗       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║ \x1b[95m█\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗  \x1b[95m███████\x1b[94m║\x1b[95m█████\x1b[94m╔╝ \x1b[95m█████\x1b[94m╗  \x1b[95m██████\x1b[94m╔╝\n    \x1b[95m██\x1b[94m║╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝   \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║╚════\x1b[95m██\x1b[94m║       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔═\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m║ ╚\x1b[95m████\x1b[94m║\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╔╝ \x1b[95m██\x1b[94m╗╚\x1b[95m██████\x1b[94m╔╝\x1b[95m███████\x1b[94m║       \x1b[95m██\x1b[94m║   ╚\x1b[95m███\x1b[94m╔\x1b[95m███\x1b[94m╔╝\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\n    \x1b[94m╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
        print('   ', '\x1b[95mDeveloped by \x1b[94mThorstellinii', '                 ', '\x1b[90mVersion: 1.0')
        print('                                          ', '\x1b[92mLast Updated: 21.10.2024')
        print('\x1b[94m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('                                     ', '\x1b[97mLogged in as:\x1b[91m', say_license())
        print()
        print('\x1b[95mDebloater \x1b[94m>')
        print()
        print('\x1b[95m[\x1b[94m1\x1b[95m]\x1b[94m-\x1b[97mRemove Solitaire\x1b[0m', '          ', '\x1b[95m[\x1b[94m8\x1b[95m]\x1b[94m-\x1b[97mRemove Smartphone Link\x1b[0m')
        print('\x1b[95m[\x1b[94m2\x1b[95m]\x1b[94m-\x1b[97mRemove Cortana\x1b[0m', '            ', '\x1b[95m[\x1b[94m9\x1b[95m]\x1b[94m-\x1b[97mRemove Snipping Tool\x1b[0m')
        print('\x1b[95m[\x1b[94m3\x1b[95m]\x1b[94m-\x1b[97mRemove Game Bar\x1b[0m', '           ', '\x1b[95m[\x1b[94m10\x1b[95m]\x1b[94m-\x1b[97mRemove Calculator\x1b[0m')
        print('\x1b[95m[\x1b[94m4\x1b[95m]\x1b[94m-\x1b[97mRemove Get Help\x1b[0m', '           ', '\x1b[95m[\x1b[94m11\x1b[95m]\x1b[94m-\x1b[97mRemove Office\x1b[0m')
        print('\x1b[95m[\x1b[94m5\x1b[95m]\x1b[94m-\x1b[97mRemove Sticky Notes\x1b[0m', '       ', '\x1b[95m[\x1b[94m12\x1b[95m]\x1b[94m-\x1b[97mRemove Feedback Hub\x1b[0m')
        print('\x1b[95m[\x1b[94m6\x1b[95m]\x1b[94m-\x1b[97mRemove Movies & TV\x1b[0m', '        ', '\x1b[95m[\x1b[94m13\x1b[95m]\x1b[94m-\x1b[97mToDo\x1b[0m')
        print('\x1b[95m[\x1b[94m7\x1b[95m]\x1b[94m-\x1b[97mRemove Paint\x1b[0m')
        print()
        print('\x1b[95m[\x1b[94mA\x1b[95m]\x1b[94m-\x1b[97mRemove all preinstalled apps')
        print()
        print('\x1b[95m[\x1b[94mB\x1b[95m]\x1b[94m-\x1b[97mGo Back')
        print('\x1b[95m[\x1b[94mX\x1b[95m]\x1b[94m-\x1b[97mClose')
        print()
        debloater_input = input('\x1b[95mChoose an Option \x1b[94m>\x1b[97m')
        if debloater_input == 'X' or debloater_input == 'x':
            sys.exit()
        else:
            if debloater_input == 'B' or debloater_input == 'b':
                os.system('cls')
                return
            if debloater_input == 'A' or debloater_input == 'a':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '1':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '2':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '3':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '4':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '5':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '6':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '7':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '8':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '9':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '10':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '11':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '12':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif debloater_input == '13':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            else:
                print('\x1b[91mInvalid option! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')