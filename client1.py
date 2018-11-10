import socket, sys, time, select	#for sockets

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;

currACK = 0
packet = 0
window = 4
packets = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6', 'Test 7', 'Test 8']

for packet in packets:
	msg = packet
	if currACK == 1:
		checksum = 'hi'
	else:
		checksum = ip_checksum(msg)
	currACK += 1

	try:
		s.sendto(str())

while(1) :
	msg = raw_input('Enter message to send : ')
	packet = currACK % 4
	if currACK == 1:
		checksum = 'hi'
	else:
		checksum = ip_checksum(msg)
	currACK += 1

	try :
		#Set the whole string
		s.sendto(msg, (host, port))
		s.settimeout(10)
		try:
			# receive data from client (data, addr)
			d = s.recvfrom(1024)
			reply = d[0]
			addr = d[1]
		except socket.timeout:
			checksum = ip_checksum(msg)
		print 'Server reply : ' + reply
	
	except socket.error, msg:
		print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()
