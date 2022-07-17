#
# NAME      : pwsh-ahk.py
# AUTHOR    : Robert James Patterson
# DATE      : 07/14/2022
# SYNOPSIS  : Setup the Powershell environment to allow .ps1 scripts to be executed.
# <<change>>

from ahk import AHK
from ahk.directives import NoTrayIcon

ahk = AHK(directives=[NoTrayIcon])

ps_run = 'Run powershell.exe'
ahk.run_script(ps_run, blocking=False)
ahk.find_window_by_title(b'Administrator: Windows PowerShell')
ahk.send("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser{Enter}")
ahk.send("Y{Enter}")
ahk.send("Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine{Enter}")
ahk.send("Y{Enter}")
ahk.send("Exit{Enter}")


