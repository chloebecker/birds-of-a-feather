
import os

hostname = "team12.softwareengineeringii.com"
response = os.system("ping -c 1 " + hostname)

def pingTest():
	if response == 0:
	  print(hostname, 'is up!')
	else:
	  print(hostname, 'is down!')

def runTests():
	pingTest()


runTests()