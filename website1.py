#!/usr/bin/python
import socket
import sqlite3
HOST,PORT = '', 8888
listen_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.bind((HOST, PORT))
listen_socket.listen(10)
print 'Serving HTTP on port %s ...' % PORT
conn = sqlite3.connect('switchgear.db')
vals=""
while True:
	client_connection, client_address = listen_socket.accept()
	request = client_connection.recv(1024)
	print request
	print client_address
	if request == "fsdfd":	
		cursor = conn.execute("SELECT * FROM METER WHERE NAME = 'METER_A4';")
		for row in cursor:			
			vals=','.join(str(x) for x in row)+' '
			print vals
		client_connection.send(vals)
	elif request == "32423":
		http_response = "24,25,26 "
		print '24,25,26 '
		client_connection.send(http_response)
	else:
	 	cursor = conn.execute(request)
		counter=0
	 	for row in cursor:
			if counter==0:
				counter=counter+1			
				vals=','.join(str(x) for x in row)
				print vals
			else:
				counter=counter+1
                                vals=vals+','+','.join(str(x) for x in row)
                                print vals
		vals=vals+" "
		client_connection.send(vals)
	client_connection.close()
client_connection.close() 
