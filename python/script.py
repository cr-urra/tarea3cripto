from xycrypto.ciphers import TripleDES_OFB
import binascii

key = '3834343434443451'
iv = '1234123412341234'
plaintext = 'Aloha MADAFAKAAAA'
cipher = TripleDES_OFB(binascii.a2b_hex(key), iv= binascii.a2b_hex(iv))
msg = cipher.encrypt(plaintext.encode('utf-8'))

msgF = '"'+binascii.b2a_base64(msg).decode('utf-8')+'"'
keyF = '"'+key+'"'
ivF = '"'+iv+'"'
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
        <div class="3DES" id="""+msgF+"""></div>
        <div class="iv" id="""+ivF+"""></div>
        <div class="key" id="""+keyF+"""></div>
    </body>
</html>
"""
html.write(mensaje)
html.close()
