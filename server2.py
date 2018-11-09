import socket, sys, random, select, time
from check import ip_checksum

HOST = ''
PORT = 8888

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket Created'
except socket.error, msg:
	print 'failed to create socket. Error Code : '+ str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

try:
	s.bind((HOST,PORT))
except socket.error, msg:
	print 'Bind Failed. Error Code : ' + str(msg[0]) + ' Message ' + msg([1])
	sys.exit()

print 'Socket bind complete.'

inputs = [s]
outputs = []
timeout = 5
currACK = 0

while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    checksum = ip_checksum(data[1:-2]) # Uses only the raw string of characters

    if not data:
        break
    if data[0] != str(currACK):
        # Repeated ACK
        print 'Duplicate.'
        continue
    if (data != (str(currACK) + data[1:-2] + checksum)) and (data != (str(not currACK) + data[1:-2] + checksum)):
        # Checksum is corrupted
        print 'Corrupted data.'
        continue
    
    reply = 'ACK' + str(currACK) + ' Message:' + data[1:-2]
    currACK = 1 - currACK # 1-1=0 1-0=1

    s.sendto(reply, addr)
    print 'Message [' + addr[0] + ':' + str(addr[1]) + '] - ' + data [1:-2]

s.close()