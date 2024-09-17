import imaplib
import re

#datos
host = 'imap.gmail.com'
usuario = 'francisca.cb@gmail.com'
contraseña = 'jaleita01'
imap = imaplib.IMAP4_SSL(host)

def expresion_regular():
    f = open ('expresion.txt','r')
    i=0
    for j in f:
        if i==0:
            expresion = j
        else:
            correito = j
        i=i+1
    f.close()
    return expresion, correito


def logearse(usuario, contraseña):
    imap.login(usuario, contraseña)
    return 


def buscar_correo_matchar(correito, expresion):

    imap.select('Inbox')
    typ, data = imap.search(None,'FROM', correito) 
    for num in data[0].split():
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        datito= data[0][1].decode()
        datito=datito.replace("Message-ID:", "")
        datito=datito.replace(">", "")
        datito=datito.replace("<", "")
        datito=datito.replace("Message-Id:", "")
        datito=datito.strip()
        print(datito)
        correito = correito.strip()
        expresion = expresion.strip()
        a=re.fullmatch(expresion,datito)
        if a != None:
            print("match")
        else:
            print(" no match")



a, b= expresion_regular()
logearse(usuario, contraseña)
buscar_correo_matchar(b, a)
imap.close()
