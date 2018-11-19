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
done = 0
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
	if done == 0:
		if num == 0:
			#Send first 4 original packets
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
				# received += 1
				reply = d[0]
				addr = d[1]
				print(reply)

				if (reply != 'ACK: ' + packets[currLeft]):
					print('Wrong ACK')
					socket.timeout
				elif (reply == 'ACK: ' + packets[7]):
					done = 1
				else:
					# FIXME Implement move window over, send new data, and reset timeout
					currLeft += 1
					if currLeft <= len(packets) - window:
						#Window does not move
						msg = packets[currLeft + window - 1]
					else:
						print(currLeft)
					if num < 8:
						s.sendto(msg, (host, port))
						print 'Sending: ' + str(msg)
						num += 1
			except socket.timeout:
				print 'Timeout occurred. Resending all packets in window.'
				print 'Current window: ' + str(currLeft) + '-' + str(currLeft + window)
				for i in range(currLeft, window + 1):
					msg = packets[i]
					try:
						s.sendto(msg, (host, port))
						print('Sending packet: ' + str(i + 1) + ' again..')
						if i == 0:
							s.settimeout(10)
					except socket.error, msg:
						print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
						sys.exit()
	else:
		msg = raw_input('Please enter a message to send to the server: ')
		try:
			s.sendto(msg, (host, port))
			s.settimeout(10)
			print'Sending: ' + str(msg)
		except socket.error, msg:
			print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
			sys.exit()

		try:
			d = s.recvfrom(1024)
			reply = d[0]
			addr = d[1]
			if reply == 'ACK: exit()':
				print 'Goodbye.'
				sys.exit()
			else:
				print(reply)
		except socket.timeout:
			print 'Timeout occurred after the GBN.'
			print 'Exiting...'
			sys.exit()