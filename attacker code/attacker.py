import socket 

def socket_create():
    try:
        host='localhost'
        port =9999
        global  s
        s=socket.socket() 
        s.bind((host,port))
        s.listen(5)
        print("[+] Listening for incoming TCP connections on Port 9999 ")
        
    except socket.error as msg:
        print("Socket creation error: "+str(msg))
    
def socket_accept():
    conn,addr=s.accept()
    print("Connection Established | IP : ",str(addr[0])," | PORT : ",str(addr[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    print("Shell >",end="")
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            exit()                                                                                                           
        if len(cmd)>0:
            conn.send(bytes(cmd,'utf-8'))
            client_response=str(conn.recv(1024).decode('utf-8'))
            print(client_response.strip('\r\n'),end="")

            # print(client_response,end="")

if __name__=="__main__":
    socket_create()
    socket_accept()
    



