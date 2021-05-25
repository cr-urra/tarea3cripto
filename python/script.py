from xycrypto.ciphers import TripleDES_OFB
import binascii
import base64
from Crypto import Random

key = '3834343434443456'
iv = '1234123412341234'
plaintext = 'SupErCaliFRAGIlisTICOESpirALiDOsos'
cipher = TripleDES_OFB(binascii.a2b_hex(key.encode('utf-8')), iv= binascii.a2b_hex(iv.encode('utf-8')))
msg = cipher.encrypt(plaintext.encode('utf-8'))

msgF = '"'+base64.b64encode(msg).decode('utf-8')+'"'
keyF = '"'+key+'"'
ivF = '"'+iv+'"'
print(msgF)
html = open('../index.html','w')
mensaje = """<!DOCTYPE html>
<html lang="es" style="background-color: black; color: white;">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tarea 3 Criptografia y seguridad en redes</title>
    </head>
    <body>
        <p>Este sitio contiene un mensaje secreto</p>
        <div class="algorithm" id="""+msgF+"""></div>
        <div class="iv" id="""+ivF+"""></div>
        <div class="key" id="""+keyF+"""></div>
    </body>
</html>
"""
html.write(mensaje)
html.close()
