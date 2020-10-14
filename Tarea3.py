import blowfish
import binascii
import base64
from os import urandom

cipher = blowfish.Cipher(b'patata')
data = b'salchipapas' #data to encrypt, multiplo de 8
iv = b'mensajee' # initialization vector, tiene que ser 8
#iv = urandom(8)

data_encrypted = b"".join(cipher.encrypt_cfb(data, iv))

#data_encrypted_b64 = base64.b64encode(data_encrypted)#b64
#data_decrypted_b64 = base64.b64decode(data_encrypted_b64)#b64 decode

data_encryptedb_hex = binascii.hexlify(data_encrypted) #hexadecimal

#data_decrypted = b"".join(cipher.decrypt_cfb(data_encrypted, iv))#desencriptar

#data_decrypted2 = data_decrypted.decode() #mensaje original sin "b"
#cipher_b64 = data_encrypted_b64.decode() #b64 sin "b"
print(data_encryptedb_hex)


a="""<html>
<head></head>
<body>
<p>Este sitio contiene un mensaje secreto </p>
<div class="blowfish" id="""+str(data_encryptedb_hex)+"""></div>
<div class= "iv" id= """+str(iv)+"""></div>
</body>
</html>"""

with open(r"a.html", 'w') as paginita:
    paginita.write(a)


