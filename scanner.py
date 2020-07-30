#!/bin/python3
import sys        #allows us to enter command line args
import socket     
from datetime import datetime as dt

#Define the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Transalates host name to IPV4
else:
	print("Invalid . Two arguments reqd")
	print("Syntax: python3 scanner.py <ip>")
	sys.exit()
	
#Adding a line like banner
print("-" * 50)
print("Scanning target "+target)
print("Time started:"+str(dt.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET:IPV$ and SOCK_STREAM:port
		socket.setdefaulttimeout(1) 
		result = s.connect_ex((target,port))    #returns error
		print("Checking port {}".format(port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
except socket.error:
	print("Couldnt connect to server")
	sys.exit()
