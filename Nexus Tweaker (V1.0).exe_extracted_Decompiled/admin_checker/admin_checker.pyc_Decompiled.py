# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import ctypes
import colorama
colorama.init()

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()
if is_admin():
    print('\x1b[41m\x1b[97mImportant Notice Regarding Program Usage')
    print()
    print('\x1b[41m\x1b[97mWarning: Errors may occur while using this program that could potentially damage your device.')
    print('\x1b[41m\x1b[97mPlease be aware that the developer is not liable for any damages or losses resulting from the use of')
    print('\x1b[41m\x1b[97mthis program. Using this program is at your own risk.')
    print('')
    print('\x1b[41m\x1b[97mTo confirm that you have read and understood this notice, please type "I AGREE" in all capital letters.')
    print('\x1b[41m\x1b[97mIf you do not agree, please press the Enter key to exit the program.')
    print('\x1b[0m')
    response_input = input('your response:')
    if response_input == 'I AGREE':
        os.system('cls')
        from start_menu import start_menu
    else:
        sys.exit()
else:
    print('\x1b[41m\x1b[97mRUN AS ADMINISTRATOR.\x1b[0m')
    input('Press Enter key to Close!')