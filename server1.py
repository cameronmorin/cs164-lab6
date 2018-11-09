import socket
import sys

HOST = ''
PORT = 8888

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' Message ' + str(msg[1])
    sys.exit()

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print 'Bind failed. Error code : ' + str(msg[0]) + ' Message ' + str(msg[1])
    sys.exit()

print 'Socket bind complete.'

currACK = 0

while 1:
    # receive data from the client (data, addr)
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]

    if not data:
        break
    
    if currACK == 0:
        reply = 'ACK0: OK...' + data
        currACK = 1
    else:
        reply = 'ACK1: OK...' + data
        currACK = 0
        
    s.sendto(reply, addr)
    print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()

s.close()