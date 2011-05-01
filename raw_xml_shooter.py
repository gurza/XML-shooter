# Simple raw XML shooter (use socket)
# Work with localserver, server port is command line initial parameter.
#
# usage:
# 	python raw_xml_shooter.py [srv_port]
#

import sys
import socket

def main():
	xml_msg = """<xml version="1.0" encoding="UTF-8">
	<scheme>
		<elm1>test</elm1>
	</scheme>
	"""

	srv_host = 'localhost'
	try:
		srv_port = int(sys.argv[1])
	except:
		print "usage %s [srv_port]" % (sys.argv[0])
		sys.exit()

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((srv_host, srv_port))
	s.send("GET / HTTP/1.0\r\n")
	s.send("Content-Type: text/xml\r\n")
	s.send("Content-Length: "+str(len(xml_msg))+"\r\n\r\n")
	s.send(xml_msg)

	resp = s.recv(1024)
	print resp
	s.close()

if __name__=='__main__':
	main()
