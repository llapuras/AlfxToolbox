set "zip=C:\Program Files\7-Zip\7z.exe"
for /r %%i in ("*.zip") do (
"%zip%" x %%i -y -aos -o"*\"
)