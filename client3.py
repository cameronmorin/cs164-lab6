import socket, sys, time, select
from check import ip_checksum

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()

host = 'localhost';
port = 8888;

#Expected ACK
packet = 0

while(1):
    msg = raw_input('Enter Message to send : ')
    checksum = ip_checksum(msg)
	
    try:
        s.sendto(str(packet) + msg + checksum, (host, port))	
        #Set timeout length
        s.settimeout(10)

        try:
            # Receive incoming data from server
            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]
        except socket.timeout: # If timeout before getting response
            print 'Re-sending...'
            #Reset the checksum
            checksum = ip_checksum(msg)
            #Resend the data to the server
            s.sendto(str(packet) + msg + checksum, (host, port))

            d = s.recvfrom(1024)
            reply = d[0]
            addr = d[1]

        print 'Server reply: ' + reply
        packet = 1 - packet

    except socket.error, msg: 
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()