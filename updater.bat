@echo off

set "github_repo=https://github.com/charlie-sans/Open-NBS-VR"
set "local_folder=%~dp0repo"

echo Cloning repository...
git clone %github_repo% %local_folder%
echo Done.

echo Updating files...
robocopy %local_folder% %~dp0 /E /IS /IT /XO
echo Done.

echo Setting folder permissions...
icacls %local_folder% /grant:r %USERNAME%:(OI)(CI)F /T /Q
echo Done.

pause
