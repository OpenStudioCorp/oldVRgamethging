@echo off
REM Check if script is running with admin privileges
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :admin
) else (
    goto :elevate
)

:admin
REM Delete the folder in the same directory as the script
rd /s /q "%~dp0\folder-to-delete"
goto :eof

:elevate
REM Elevate to admin through UAC
if exist "%temp%\getadmin.vbs" (
    goto :gotAdmin
)
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
del "%temp%\getadmin.vbs"
goto :eof

:gotAdmin
REM Call this script again with admin privileges
"%~s0" admin
goto :eof
