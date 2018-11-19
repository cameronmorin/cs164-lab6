import socket, sys, time, select	#for sockets

# create dgram udp socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;

currLeft = 0		#Current left bound index of the window
window = 4
num = 0
received = 0
packets = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6', 'Test 7', 'Test 8']

# for packet in packets:
# 	msg = packet
# 	if currACK == 1:
# 		checksum = 'hi'
# 	else:
# 		checksum = ip_checksum(msg)
# 	currACK += 1

# 	try:
# 		s.sendto(str())

while(1) :
	if num == 0:
		for i in range(currLeft, window):
			msg = packets[i]
			# checksum = ip_checksum(msg)
			try:
				s.sendto(msg, (host, port))
				print('Sending packet: ' + str(i + 1))
				num += 1
				if i == 0:		#Set timeout on first packet sent
					s.settimeout(10)
			except socket.error, msg:
				print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
				sys.exit()
	
	if received < 8:
		try:
			d = s.recvfrom(1024)
			received += 1
			reply = d[0]
			addr = d[1]
			print(reply)

			# FIXME Implement move window over, send new data, and reset timeout
			currLeft += 1
			if currLeft <= len(packets) - window:
				#Window does not move
				msg = packets[currLeft + window - 1]
			else:
				print(currLeft)
			if num < 8:
				s.sendto(msg, (host, port))
				print(msg)
				num += 1
		except socket.timeout:
			print 'Timeout occurred. Resending all packets in window.'
			print 'Current window: ' + str(currLeft) + '-' + str(currLeft + window)
			for i in range(currLeft, window):
				msg = packets[i]
			# FIXME resend all packets in current window

	# packet = currACK % 4
	# if currACK == 1:
	# 	checksum = 'hi'
	# else:
	# 	checksum = ip_checksum(msg)
	# currACK += 1

	# try :
	# 	#Set the whole string
	# 	s.sendto(msg, (host, port))
	# 	s.settimeout(10)
	# 	try:
	# 		# receive data from client (data, addr)
	# 		d = s.recvfrom(1024)
	# 		reply = d[0]
	# 		addr = d[1]
	# 	except socket.timeout:
	# 		checksum = ip_checksum(msg)
	# 	print 'Server reply : ' + reply
	
	# except socket.error, msg:
	# 	print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	# 	sys.exit()
