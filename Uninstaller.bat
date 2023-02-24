@echo off

set "local_folder=%~dp0repo"

echo Uninstalling folder...
rmdir /s /q "%local_folder%"
echo Done.

pause
  