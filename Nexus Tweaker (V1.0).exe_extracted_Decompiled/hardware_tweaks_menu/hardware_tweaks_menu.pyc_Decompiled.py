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

def hardware_tweaks_menu():
    while True:
        print('\n    \x1b[95m███\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╗   \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗    \x1b[95m████████\x1b[94m╗\x1b[95m██\x1b[94m╗    \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗ \x1b[95m█████\x1b[94m╗ \x1b[95m██\x1b[94m╗  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██████\x1b[94m╗ \n    \x1b[95m████\x1b[94m╗  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝    ╚══\x1b[95m██\x1b[94m╔══╝\x1b[95m██\x1b[94m║    \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║ \x1b[95m██\x1b[94m╔╝\x1b[95m██\x1b[94m╔════╝\x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗   ╚\x1b[95m███\x1b[94m╔╝ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███████\x1b[94m╗       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║ \x1b[95m█\x1b[94m╗ \x1b[95m██\x1b[94m║\x1b[95m█████\x1b[94m╗  \x1b[95m███████\x1b[94m║\x1b[95m█████\x1b[94m╔╝ \x1b[95m█████\x1b[94m╗  \x1b[95m██████\x1b[94m╔╝\n    \x1b[95m██\x1b[94m║╚\x1b[95m██\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝   \x1b[95m██\x1b[94m╔\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║╚════\x1b[95m██\x1b[94m║       \x1b[95m██\x1b[94m║   \x1b[95m██\x1b[94m║\x1b[95m███\x1b[94m╗\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m╔═\x1b[95m██\x1b[94m╗ \x1b[95m██\x1b[94m╔══╝  \x1b[95m██\x1b[94m╔══\x1b[95m██\x1b[94m╗\n    \x1b[95m██\x1b[94m║ ╚\x1b[95m████\x1b[94m║\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m╔╝ \x1b[95m██\x1b[94m╗╚\x1b[95m██████\x1b[94m╔╝\x1b[95m███████\x1b[94m║       \x1b[95m██\x1b[94m║   ╚\x1b[95m███\x1b[94m╔\x1b[95m███\x1b[94m╔╝\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m╗\x1b[95m███████\x1b[94m╗\x1b[95m██\x1b[94m║  \x1b[95m██\x1b[94m║\n    \x1b[94m╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝       ╚═╝    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝')
        print('   ', '\x1b[95mDeveloped by \x1b[94mThorstellinii', '                 ', '\x1b[90mVersion: 1.0')
        print('                                          ', '\x1b[92mLast Updated: 21.10.2024')
        print('\x1b[94m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('                                     ', '\x1b[97mLogged in as:\x1b[91m', say_license())
        print()
        print('\x1b[95mHardware Tweaks \x1b[94m>')
        print()
        print('\x1b[95m[\x1b[94m1\x1b[95m]\x1b[94m-\x1b[97mCPU \x1b[95m(\x1b[94mSet CPU to maximum performance\x1b[95m)\x1b[0m')
        print('\x1b[95m[\x1b[94m2\x1b[95m]\x1b[94m-\x1b[97mGPU\x1b[95m(\x1b[94mSet GPU to maximum performance\x1b[95m)\x1b[0m')
        print('\x1b[95m[\x1b[94m3\x1b[95m]\x1b[94m-\x1b[97mGPU\x1b[95m(\x1b[94mAMD\x1b[95m)\x1b[0m')
        print('\x1b[95m[\x1b[94m4\x1b[95m]\x1b[94m-\x1b[97mRAM \x1b[95m(\x1b[94mSet RAM to maximum performance\x1b[95m)\x1b[0m')
        print('\x1b[95m[\x1b[94m5\x1b[95m]\x1b[94m-\x1b[97mSSD \x1b[95m(\x1b[94mSet SSD to maximum performance\x1b[95m)\x1b[0m')
        print('\x1b[95m[\x1b[94m6\x1b[95m]\x1b[94m-\x1b[97mMouse and Keyboard Tweaks')
        print()
        print('\x1b[95m[\x1b[94mB\x1b[95m]\x1b[94m-\x1b[97mGo Back')
        print('\x1b[95m[\x1b[94mX\x1b[95m]\x1b[94m-\x1b[97mClose')
        print()
        hardware_tweaks_input = input('\x1b[95mChoose an Option \x1b[94m>\x1b[97m')
        if hardware_tweaks_input == 'X' or hardware_tweaks_input == 'x':
            sys.exit()
        else:
            if hardware_tweaks_input == 'B' or hardware_tweaks_input == 'b':
                os.system('cls')
                return
            if hardware_tweaks_input == '1':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif hardware_tweaks_input == '2':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif hardware_tweaks_input == '3':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif hardware_tweaks_input == '4':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif hardware_tweaks_input == '5':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            elif hardware_tweaks_input == '6':
                print('\x1b[91mThis tweak is not available in the free version! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')
            else:
                print('\x1b[91mInvalid option! (Wait 2 seconds)')
                time.sleep(2)
                os.system('cls')