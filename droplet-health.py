import os

dropletIp = "206.189.166.76"

def dropletHealth():
	print("\n-----------  BEGIN TEST CASE: dropletHealth()  -----------\n")
	print("\nMaking request to " + dropletIp + "... ... ...")
	print("------------------------------------------------------------\n")
	## tidy -i formats output with indentation so it's easier to read
	os.system("curl " + dropletIp + " | tidy -i")

	## grep uses regex to find given text in the input file (in our case, the html for page we
	## 		performed a get request on with cURL)
	grepTxt = "\"<p>If you see this page, the nginx web server is successfully installed\""
	print("\nSearching html with grep" + dropletIp + "... ... ...")
	print("------------------------------------------------------------\n")

	response = os.system("curl " + dropletIp + " | grep " + grepTxt)
	
	print("\nRESPONSE:")
	print("------------------------------------------------------------\n")
	if response == 0:
		print(dropletIp + " is running!")
	else:
		print(dropletIp + " may be down, please check the droplet.")
	print("\n-----------  END OF TEST CASE: dropletHealth()  -----------\n")
	

def runTests():
	dropletHealth()


runTests()