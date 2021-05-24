from xtea3 import *
import base64

key = b"bQeThVmYq3t6w9z$"  # Never use this
text = b"SupeCaliCaliCali"
iv = b"12345678"
x = new(key, mode=MODE_ECB, IV=iv)
c = x.encrypt(text)
text == x.decrypt(c)
msg = base64.b64encode((str(len(iv))+iv.decode('utf-8')).encode('utf-8')+c)
print(msg)
print(base64.b64decode(msg))

msgF = '"'+msg.decode('utf-8')+'"'
html = open('../index.html','w')
mensaje = """<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tarea 3 Criptografia y seguridad en redes</title>
    </head>
    <body>
        <p>Este sitio contiene un mensaje secreto</p>
        <div class="algorithm" id="""+msgF+"""></div>
    </body>
</html>
"""
html.write(mensaje)
html.close()


