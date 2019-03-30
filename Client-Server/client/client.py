"""
    First of all, sorry for my bad english
    Bugs developed by: Rodrigo Bisso (this code works, it's just a joke haha :D)
    Student in Universidade Federal do Pampa (UNIPAMPA), Brasil
"""

import socket
import sys
import threading
import os
import struct
    
def send_file(name, HOST, PORT, filename):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST,PORT))

    #sending size of file's name
    size_filename = len(filename)
    sock.send(struct.pack('i', size_filename))
    
    #sending file's name
    sock.send(filename.encode())
    
    #sending file's content
    with open(filename, 'rb') as f:
        bytes_to_send = f.read(1024)
        while bytes_to_send:
            sock.send(bytes_to_send)
            bytes_to_send = f.read(1024)

    sock.close()
    
def usage():
    print("Usage:")
    print("\tpython3 "+sys.argv[0]+" <ip> <port> <files>")
    print("\tfor ip and port, look the variables HOST and PORT on the server.py file")
def main():
    
    if len(sys.argv) < 3:
        usage()
        sys.exit()
    
    print (sys.argv[3:])
    for arg in sys.argv[3:]:
        print(arg)
        t = threading.Thread(target=send_file, args=("send_file",sys.argv[1],int(sys.argv[2]),arg))
        t.start()
    
if __name__ == '__main__':
    main()
