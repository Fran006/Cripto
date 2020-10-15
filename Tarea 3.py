import blowfish
import binascii
import base64
from os import urandom

print( "Mensaje:")
data=input()
print( "Clave:")
key= input()
var = True
while var:
    print( "Iv (solo de 8 caracteres):")
    iv= input()
    p= len(iv)
    if p==8:
       var=False


cipher = blowfish.Cipher(key.encode("utf-8"))
        
data_encrypted = b"".join(cipher.encrypt_cfb(data.encode("utf-8"), iv.encode("utf-8")))
print(data_encrypted)

#data_encrypted_b64 = base64.b64encode(data_encrypted)#b64
#data_decrypted_b64 = base64.b64decode(data_encrypted_b64)#b64 decode

data_encryptedb_hex = binascii.hexlify(data_encrypted) #hexadecimal
print(data_encryptedb_hex)

#data_decrypted = b"".join(cipher.decrypt_cfb(data_encrypted, iv))#desencriptar
#data_encryptedb_hex2= data_encryptedb_hex.decode()

#data_decrypted2 = data_encryptedb_hex.decode()
#iv2 = iv.decode()#mensaje original sin "b"
#cipher_b64 = data_encrypted_b64.decode() #b64 sin "b"
#print(data_decrypted2)
#print(iv2)



a="""
<p>Este sitio contiene un mensaje secreto </p>
<div class="blowfish" id="""+str(data_encrypted)+"""></div>
<div class= "iv" id= """+iv+"""></div>
<div class= "llave" id= """+key+"""></div>"""

with open(r"a.html", 'w') as paginita:
    paginita.write(a)


