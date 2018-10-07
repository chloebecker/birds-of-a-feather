import os

droplet = "https://team12.softwareengineeringii.com/"

def dropletHealth():
	print("\n-----------  BEGIN TEST CASE: dropletHealth()  -----------\n")
	print("\nMaking request to " + droplet + "... ... ...")
	print("------------------------------------------------------------\n")
	## tidy -i formats output with indentation so it's easier to read
	os.system("curl " + droplet + " | tidy -i")

	## grep uses regex to find given text in the input file (in our case, the html for page we
	## 		performed a get request on with cURL)
	grepTxt = "\"<h1>Success\""
	print("\nSearching html with grep" + droplet + "... ... ...")
	print("------------------------------------------------------------\n")

	response = os.system("curl " + droplet + " | grep " + grepTxt)
	
	print("\nRESPONSE:")
	print("------------------------------------------------------------\n")
	if response == 0:
		print(droplet + " is running!")
	else:
		print(droplet + " may be down, please check the droplet.")
	print("\n-----------  END OF TEST CASE: dropletHealth()  -----------\n")
	

def runTests():
	print("----------------------------------------")
	print("-------------  Test Menu:  -------------")
	print("----------------------------------------")
	op = ""
	while op != "e":
		print("Options:")
		print("1 - Droplet Health")
		print("e - Exit")
		op = input("")
		if(op == "1"):
			dropletHealth()
		elif(op == "e"):
			print("\nBye!")
			return
		else:
			print("Invalid choice. Try again.\n")


runTests()