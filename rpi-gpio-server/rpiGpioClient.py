import socket
import sys
import time

def connectToSocket(hostname, port):
    HOST = hostname # The remote host
    PORT = port # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    
        af, socktype, proto, canonname, sa = res
    
        try:
            s = socket.socket(af, socktype, proto)
    
        except socket.error, msg:
            s = None
            continue
    
        try:
            s.connect(sa)
    
        except socket.error, msg:
            s.close()
            s = None
            continue
    
        break
    
    if s is None:
        print "could not open socket"
        sys.exit(1)

    return s

s = connectToSocket("p45-pi-01.diamond.ac.uk", 50007)
s.send("29,n,o,None,0")
data = s.recv(1024)
print data
s.send("29,s,o,PULSE,1000")
data = s.recv(1024)
print data
s.send("1,n,i,None,0")
try:
    while True:
        s.send("1,g,i,None,0")
        data = s.recv(1024)
        print data
        #time.sleep(1)
finally:        
    s.close()
