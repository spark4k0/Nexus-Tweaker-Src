# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import subprocess
import time
import colorama
colorama.init()
import os
import shutil
import subprocess
import winreg

def disable_windows_search_indexing():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Stop-Service -Name \"WSearch\" -Force'])
    subprocess.run(['powershell', '-Command', 'Set-Service -Name \"WSearch\" -StartupType Disabled'])
    print('[94mWindows search indexing has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_game_bar():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Get-AppxPackage Microsoft.XboxGamingOverlay | Remove-AppxPackage'])
    print('[94mXbox Game Bar has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_visual_effects_and_more():
    print('[94mPlease wait...')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name \'DragFullWindows\' -Value 0; Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name \'UserPreferencesMask\' -Value ([byte[]](0x90,0x12,0x03,0x80,0x10,0x00,0x00,0x00)); Set-ItemProperty -Path \'HKCU:\\Control Panel\\Desktop\' -Name \'VisualFXSetting\' -Value 2; Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\' -Name \'DisableAnimations\' -Value 1; Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize\' -Name \'EnableTransparency\' -Value 0'])
    print('[94mVisual effects have been optimized for best performance! (Wait 2 seconds)')
    time.sleep(2)

def disable_windows_tips_and_suggestions():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \"HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" -Name \"SystemPaneSuggestionsEnabled\" -Value 1; Set-ItemProperty -Path \"HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager\" -Name \"SubscribedContent-338388Enabled\" -Value 1'])
    print('[94mWindows tips and suggestions have been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_cortana():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Get-AppxPackage -Name Microsoft.549981C3F5F10 | Remove-AppxPackage'])
    print('[94mCortana has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def update_windows():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'start ms-settings:windowsupdate'])
    print('[94mWindows has been checked for updates! (Wait 2 seconds)')
    time.sleep(2)

def disable_hibernation():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'powercfg -h off'])
    print('[94mHibernation has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_superfetch():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Stop-Service -Name SysMain'])
    subprocess.run(['powershell', '-Command', 'Set-Service -Name SysMain -StartupType Disabled'])
    print('[94mSuperfetch has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def turn_off_uac():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \"HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System\" -Name \"EnableLUA\" -Value 0'])
    print('[94mUAC has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_remote_assistance():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\' -Name \'fAllowToGetHelp\' -Value 0'])
    print('[94mRemote Assistance has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def turn_off_windows_error_reporting():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Stop-Service -Name \"WerSvc\" -Force'])
    subprocess.run(['powershell', '-Command', 'Set-Service -Name \"WerSvc\" -StartupType Disabled'])
    print('[94mWindows Error Reporting has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_windows_ink_space():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \"HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced\" -Name \"DisabledHotkeys\" -Value \" \"'])
    print('[94mWindows Ink Space has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def disable_prefetch():
    print('[94mPlease wait...')
    print('[92m')
    subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path \"HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\" -Name \"PrefetchParameters\" -Value 0'])
    print('[94mPrefetch has been disabled! (Wait 2 seconds)')
    time.sleep(2)

def optmimize_scheduled_tasks():
    schtasks_commands = ['schtasks /delete /f /tn \"\\Microsoft\\Windows\\WindowsUpdate\\Scheduled Start\" >nul 2>&1', 'schtasks /delete /f /tn \"\\Microsoft\\Windows\\UpdateOrchestrator\\Schedule Scan\" >nul 2>&1', 'schtasks /delete /f /tn \"\\Microsoft\\Windows\\UpdateOrchestrator\\Schedule Scan Static Task\" >nul 2>&1', 'schtasks /delete /f /tn \"\\Microsoft\\Windows\\UpdateOrchestrator\\Schedule Wake To Work\" >nul 2>&1', 'schtasks /delete /f /tn \"\\Microsoft\\Windows\\UpdateOrchestrator\\Start Oobe Expedite Work\" >nul 2>&1', 'schtasks /Change /TN \"Microsoft\\Windows\\ErrorDetails\\EnableErrorDetailsUpdate\" /Disable >nul 2>&1', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Error Reporting\\QueueReporting\" /Disable >nul 2>&1', 'schtasks /Change /TN \"\\Microsoft\\Windows\\Application Experience\\AitAgent\" /DISABLE >nul', 'schtasks /Change /TN \"\\Microsoft\\Windows\\Media Center\\ehDRMInit\" /DISABLE > nul', 'schtasks /change /TN NvTmMon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8} /DISABLE', 'schtasks /change /TN NvTmRep_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8} /DISABLE', 'schtasks /change /TN NvTmRepOnLogon_{B2FE1952-0186-46C3-BAEC-A80AA35AC5B8} /DISABLE', 'schtasks /change /TN \"Microsoft\\Office\\OfficeTelemetryAgentFallBack\" /DISABLE', 'schtasks /change /TN \"Microsoft\\Office\\OfficeTelemetryAgentFallBack2016\" /DISABLE', 'schtasks /change /TN \"Microsoft\\Office\\OfficeTelemetryAgentLogOn\" /DISABLE', 'schtasks /change /TN \"Microsoft\\Office\\OfficeTelemetryAgentLogOn2016\" /DISABLE', 'schtasks /change /tn \"\\Microsoft\\Windows\\Windows Error Reporting\\QueueReporting\" /disable', 'schtasks /Change /TN \"Microsoft\\Windows\\AppID\\SmartScreenSpecific\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Autochk\\Proxy\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\FileHistory\\File History (maintenance mode)\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Maintenance\\WinSAT\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\NetTrace\\GatherNetworkInfo\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\PI\\Sqm-Tasks\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Time Synchronization\\ForceSynchronizeTime\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Time Synchronization\\SynchronizeTime\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Error Reporting\\QueueReporting\" /Disable', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Defender\\Windows Defender Cache Maintenance\" /Enable', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Defender\\Windows Defender Cleanup\" /Enable', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Defender\\Windows Defender Scheduled Scan\" /Enable', 'schtasks /Change /TN \"Microsoft\\Windows\\Windows Defender\\Windows Defender Verification\" /Enable', 'schtasks /Delete /TN \"\\Microsoft\\Windows\\Defrag\\ScheduledDefrag\" /F', 'schtasks /end /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\BthSQM\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\BthSQM\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\UsbCeip\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Uploader\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Customer Experience Improvement Program\\Uploader\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\Application Experience\\StartupAppTask\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\Application Experience\\StartupAppTask\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector\"', 'schtasks /change /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector\" /disable', 'schtasks /end /tn \"\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticResolver\"',
    print('[94mPlease wait...')
    print('[92m')
    for command in schtasks_commands:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f'Successfully executed: {command}')
        except subprocess.CalledProcessError as e:
            pass  # postinserted
    else:  # inserted
        print('[94mScheduled tasks are optimized! (Wait 2 seconds)')
        time.sleep(2)
        print(f'Error executing {command}: {e}')

def clean_temp():
    print('[94mPlease wait...')
    try:
        subprocess.run(['powershell', '-Command', 'cleanmgr'], check=True)
    except subprocess.CalledProcessError as e:
        pass  # postinserted
    else:  # inserted
        print('[94mCleanmanager opens! (Wait 2 seconds)')
        time.sleep(2)
        print(f'Fehler beim Öffnen des Datenträgerbereinigungsmanagers: {e}')
    else:  # inserted
        pass

def all():
    print('[94mPlease wait... (This may take a while)')
    print('[92m')
    disable_windows_search_indexing()
    disable_game_bar()
    disable_visual_effects_and_more()
    disable_windows_tips_and_suggestions()
    disable_cortana()
    disable_hibernation()
    disable_superfetch()
    turn_off_uac()
    disable_remote_assistance()
    turn_off_windows_error_reporting()
    disable_windows_ink_space()
    disable_prefetch()
    optmimize_scheduled_tasks()
    clean_temp()
    update_windows()
    clean_temp()
    print('[94mAll tasks have been completed! (Wait 2 seconds)')
    time.sleep(2)