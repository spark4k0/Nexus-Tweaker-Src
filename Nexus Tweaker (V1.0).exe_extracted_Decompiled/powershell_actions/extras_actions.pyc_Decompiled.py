# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import subprocess
import time
import colorama
colorama.init()
import subprocess

def create_restore_point():
    print('\x1b[94mPlease wait...')
    print('\x1b[92m')
    subprocess.run(['powershell', '-Command', 'Enable-ComputerRestore -Drive "C:"'])
    subprocess.run(['powershell', '-Command', 'vssadmin delete shadows /all /quiet'])
    subprocess.run(['powershell', '-Command', 'Checkpoint-Computer -Description "Nexus Tweaker Restore Point" -RestorePointType "MODIFY_SETTINGS"'])
    print('\x1b[94mRestore point was created! (Wait 2 seconds)')
    time.sleep(2)