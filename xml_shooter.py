# Simple XML shooter (use urllib)
# POST/GET parameter 'xml' contains XML command.
# Work with localserver (srv_url), server port is command line initial parameter.
#
# usage:
#   python xml_shooter.py [srv_port]
#

import sys
import urllib

def main():
	try:
		srv_port = sys.argv[1]
	except:
		print "usage %s [srv_port]" % (sys.argv[0])
		sys.exit()

	srv_url = ''.join(['http://localhost:', srv_port])
	xml_msg = """<xml version="1.0" encoding="UTF-8">
	<scheme>
		<elm1>test</elm1>
	</scheme>
	"""

	parameter = urllib.urlencode({'xml': xml_msg})
	#POST query
	resp = urllib.urlopen(srv_url,parameter)
	#GET query
	#response = urllib.urlopen(srv_url + "?%s" % parameter)
	print resp.read()


if __name__=='__main__':
	main()
