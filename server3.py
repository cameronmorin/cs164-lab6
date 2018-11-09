import socket, sys, random, select, time
from check import ip_checksum

HOST = ''
port = 8888

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket Created.'
except socket.error, msg:
    print 'Failed to create socket. Error Code : '+ str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

try:
	s.bind((HOST,port))
except socket.error, msg:
	print 'Bind Failed. Error Code : ' + str(msg[0]) + ' Message ' + msg([1])
	sys.exit()

print 'Socket bind complete'

inputs = [s]
outputs = []
#ackstatus to return the package 0/1 if received
currAck = 0
testCase = 0
#now keep talking with the client
while 1:
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
	
    #set the checksum from from the data recieved
    checksum = ip_checksum(data[1:-2])

    if not data:
        break
	#Wrong ACK
    if (data[0] != str(currAck)):
        print 'Duplicate Packet'
        continue
	#Corrupted checksum
    if (data != (str(currAck) + data[1:-2] + checksum)) and (data != (str(not ACKstatus) + data[1: -2] + checkSum)):
        print 'Corrupt'
        continue

	#check the test, set a timeout
    if testCase == 1:
        time.sleep(14)
    testCase = testCase + 1
	
    reply = 'ACK' + str(currAck) + ' Message:' + data[1:-2]
    currAck = 1 - currAck

    s.sendto(reply, addr)
    print 'Message['+ addr[0] + ':' + str(addr[1]) + '] - ' + data[1:-2]
	
s.close()