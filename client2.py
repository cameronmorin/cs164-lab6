import socket, sys, select, time
from check import ip_checksum

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;

packet = 0
numInput = 0

while(1):
	msg = raw_input('Enter Message to send : ')
	
	#numInput == 1 corrupts the checksum
	if numInput == 1:
		checkSum = ''
	else:
		checkSum = ip_checksum(msg)
	numInput = numInput + 1
	
    # Send the packet to the server: data = [ACK + msg + checksum]
	try:
		s.sendto(str(packet) + msg + checkSum, (host, port))
		s.settimeout(10)
		#Receive message from server
		try:
			d = s.recvfrom(1024)
			reply = d[0]
			addr = d[1]
		except socket.timeout:
			checksum = ip_checksum(msg)
		#if the timeout happens, send the correct packet to the server again
			s.sendto(str(packet) + msg + checksum, (host,port))
			d = s.recvfrom(1024)
			reply = d[0]
			addr = d[1]

		print 'Server message : ' + reply
		packet = 1 - packet #Alternate 1 & 0

	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + 'Message ' + msg[1]
		sys.exit()