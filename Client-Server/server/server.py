"""
    #First of all: sorry for my bad english :\
    
    Bugs developed by: Rodrigo Bisso (this code works, it's just a joke haha :D)
    Student on Universidade Federal do Pampa (UNIPAMPA) 

"""

import socket 
import sys
import threading
import os
import struct

def recv_file(name, sock):
    
    #size of the file's name

    buf = sock.recv(struct.calcsize('i'))
    size_filename = struct.unpack('i', buf)[0]
    
    print(type(size_filename), 'size_filename = ' ,size_filename)

    #reciving the file's name
    filename = sock.recv(size_filename).decode()
    
    print (filename, type(filename))
    
    #reciving file
    with open(filename,'wb') as f:
        bytes_to_recv = sock.recv(1024)
    
        while bytes_to_recv:
            f.write(bytes_to_recv)
            bytes_to_recv = sock.recv(1024)
    
    #this process is needed because the socket can send file data to the file's name
    #depending on the size of data on the file (e.g .txt files) 

def _main():
    
    HOST = ''
    PORT = 9876
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for TCP connection
    sock.bind((HOST,PORT))
    sock.listen(10)
    
    print ("Server started...")
    
    while True:
        
        conn, addr = sock.accept()
        print ("client connected with ip:<"+str(addr)+">")
        t = threading.Thread(target=recv_file, args=("recv_file", conn))
        t.start()
              
    sock.close()    

if __name__ == '__main__':
    _main()
