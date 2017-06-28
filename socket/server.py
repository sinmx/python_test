import socket
import sys
HOST = None
PORT = 8888
s = None
for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,socket.SOCK_STREAM,0,socket.AI_PASSIVE):
    af,socktype,proto,canonname,sa = res
    try:
        s = socket.socket(af,socktype,proto)
    except socket.error,err_msg:
        print err_msg
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error,err_msg:
        print err_msg
        s.close()
        s = None
        continue
    break
if s is None:
    print "could not open socket"
    sys.exit(1)
conn,addr = s.accept()
print 'connected by ',addr

while 1:
    data = conn.recv(1024)
    if not data : break
    conn.send(data)
conn.close()