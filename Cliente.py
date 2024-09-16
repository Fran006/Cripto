import socket
import sys
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey.RSA import *
from Crypto.PublicKey import RSA
import os
from time import *
import hashlib

#deshasear archivo 1 y hashear
a = "C:\\Users\\franc\\OneDrive\\Escritorio\\hashcat-6.1.1"
os.system(a)
b = "hashcat.exe -m 0 -a 0 -o patata1.txt --outfile-format=2 archivo_1 diccionario_2.dict"
tiempo_inicio= time()
os.system(b)
tiempo1 = time()-tiempo_inicio
print (tiempo1)

a2=open('patata1.txt' , 'r')
b2= open ('patata1hash.txt', 'w')
for i in a2:
 
    h = hashlib.sha3_256(i.encode()).hexdigest()
    b2.write(h+ '\n')
a2.close()
b2.close()

#deshasear archivo 2 y guardar texto
c = "C:\\Users\\franc\\OneDrive\\Escritorio\\hashcat-6.1.1"
os.system(c)
d = "hashcat.exe -m 10 -a 0 -o patata2.txt --outfile-format=2 archivo_2 diccionario_2.dict"
tiempo_inicio= time()
os.system(d)
tiempo2 = time()-tiempo_inicio
print (tiempo2)

c2=open('patata2.txt' , 'r')
d2= open ('patata2hash.txt', 'w')
for i in c2:
 
    h = hashlib.sha3_256(i.encode()).hexdigest()
    d2.write(h+ '\n')
c2.close()
d2.close()


#deshasear archivo 3 y guardar texto
e = "C:\\Users\\franc\\OneDrive\\Escritorio\\hashcat-6.1.1"
os.system(e)
f = "hashcat.exe -m 10 -a 0 -o patata3.txt --outfile-format=2 archivo_3 diccionario_2.dict"
tiempo_inicio= time()
os.system(f)
tiempo3 = time()-tiempo_inicio
print (tiempo3)

e2=open('patata3.txt' , 'r')
f2= open ('patata3hash.txt', 'w')
for i in e2:
 
    h = hashlib.sha3_256(i.encode()).hexdigest()
    f2.write(h+ '\n')
e2.close()
f2.close()

#deshasear archivo 4 y guardar texto
g = "C:\\Users\\franc\\OneDrive\\Escritorio\\hashcat-6.1.1"
os.system(g)
h = "hashcat.exe -m 1000 -a 0 -o patata4.txt --outfile-format=2 archivo_4 diccionario_2.dict"
tiempo_inicio= time()
os.system(h)
tiempo4 = time()-tiempo_inicio
print (tiempo4)

g2=open('patata4.txt' , 'r')
h2= open ('patata4hash.txt', 'w')
for i in g2:
 
    z = hashlib.sha3_256(i.encode()).hexdigest()
    h2.write(z+ '\n')
g2.close()
h2.close()

#deshasear archivo 5 y guardar texto
i = "C:\\Users\\franc\\OneDrive\\Escritorio\\hashcat-6.1.1"
os.system(i)
j = "hashcat.exe -m 1800 -a 0 -o patata5.txt --outfile-format=2 archivo_5 diccionario_2.dict"
tiempo_inicio= time()
os.system(j)
tiempo5 = time()-tiempo_inicio
print (tiempo5)

i2=open('patata5.txt' , 'r')
j2= open ('patata5hash.txt', 'w')
for w in i2:
 
    h = hashlib.sha3_256(w.encode()).hexdigest()
    j2.write(h+ '\n')
i2.close()
j2.close()


#Coneccion TCPIP
  
s = socket.socket()
Puerto= 9000
s.connect(("127.0.0.1",Puerto))
print ("conectado")

#recivo llave publica


a=eval(s.recv(4096).decode())
llave = a


cipher = PKCS1_OAEP.new(llave)
#cifrar archivo1
file1 = open('patata1hash.txt', 'r')
newfile1 = open('patata1cipher.txt', 'w')
for i in file1:
    ciphertext = cipher.encrypt(i.encode())
    newfile1.write(ciphertext.hex()+ '\n')
file1.close()
newfile1.close()
print ("archivo 1 cifrado")


#cifrar archivo2
file2 = open('patata2hash.txt', 'r')
newfile2 = open('patata2cipher.txt', 'w')
for i in file2:
    ciphertext = cipher.encrypt(i.encode())
    newfile2.write(ciphertext.hex()+ '\n')
file2.close()
newfile2.close()
print ("archivo 2 cifrado")


#cifrar archivo3
file3 = open('patata3hash.txt', 'r')
newfile3 = open('patata3cipher.txt', 'w')
for i in file3:
    ciphertext = cipher.encrypt(i.encode())
    newfile3.write(ciphertext.hex()+ '\n')
file3.close()
newfile3.close()
print ("archivo 3 cifrado")

#cifrar archivo4
file4 = open('patata4hash.txt', 'r')
newfile4 = open('patata4cipher.txt', 'w')
for i in file4:
    ciphertext = cipher.encrypt(i.encode())
    newfile4.write(ciphertext.hex()+ '\n')
file4.close()
newfile4.close()
print ("archivo 4 cifrado")

#cifrar archivo5
file5 = open('patata5hash.txt', 'r')
newfile5 = open('patata5cipher.txt', 'w')
for i in file5:
    ciphertext = cipher.encrypt(i.encode())
    newfile5.write(ciphertext.hex()+ '\n')
file5.close()
newfile5.close()
print ("archivo 5 cifrado")



#enviar archivo 1 
f1 = open('patata1cipher.txt', "r")
s.send(b"patata cipher abierto")
print("empezando archivo1")
for i in f1:    
    s.send(i.replace("\n","").encode())
    s.recv(1024).decode()
s.send(b"fin")  
print("El archivo1 ha sido enviado correctamente.")
f1.close()
msg=s.recv(1024)
print(msg.decode())
sleep(0.1)


#enviar archivo 2 
f2 = open('patata2cipher.txt', "r")
#s.send(b"patata cipher abierto")
print("empezando archivo2")
for i in f2:    
    s.send(i.replace("\n","").encode())
    s.recv(1024).decode()
s.send(b"fin")  
print("El archivo2 ha sido enviado correctamente.")
f2.close()
msg=s.recv(1024)
print(msg.decode())
sleep(0.1)
    

#enviar archivo 3 
f3 = open('patata3cipher.txt', "r")
#s.send(b"patata cipher abierto")
print("empezando archivo3")
for i in f3:    
    s.send(i.replace("\n","").encode())
    s.recv(1024).decode()
s.send(b"fin")  
print("El archivo3 ha sido enviado correctamente.")
f3.close()
msg=s.recv(1024)
print(msg.decode())
sleep(0.1)

#enviar archivo 4 
f4 = open('patata4cipher.txt', "r")
#s.send(b"patata cipher abierto")
print("empezando archivo4")
for i in f4:    
    s.send(i.replace("\n","").encode())
    s.recv(1024).decode()
s.send(b"fin")  
print("El archivo4 ha sido enviado correctamente.")
f4.close()
msg=s.recv(1024)
print(msg.decode())
sleep(0.1)

#enviar archivo 5 
f5 = open('patata5cipher.txt', "r")
#s.send(b"patata cipher abierto")
print("empezando archivo5")
for i in f5:    
    s.send(i.replace("\n","").encode())
    s.recv(1024).decode()
s.send(b"fin")  
print("El archivo5 ha sido enviado correctamente.")
f5.close()
msg=s.recv(1024)
print(msg.decode())
sleep(0.1)


s.close()
