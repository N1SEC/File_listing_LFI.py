# File_listing_LFI.py
Python script that lists interesting files on the system. 

## Use 

The script can be used to enumerate interesting files in an automated way, on systems that have **Local File Inclusion (LFI) vulnerabilities**. It is recommended that if you are looking to enumerate user private keys or user specific data, you should do it manually, as you may get better results, as this script only focuses on enumerating generic system files.

Uso:

`python3 ./File_listing_LFI.py 'http://VICTIM-HOST/index.php?=' wordlist.txt`

El script funciona colocando la URL del host vulnerable hasta el parámetro "=", luego se debe ingresar el diccionario con la lista de archivos a enumerar.

