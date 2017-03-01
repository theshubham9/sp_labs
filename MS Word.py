import sysimport win32com.client as win32

file = win32.gencache.EnsureDispatch('Word.Application')                                   #Declare vaiable openedDoc to be of type word document

filename = sys.argv[1]                                                                     #Declare variable of filename

dictionary = open ("dictionary.txt", "r")                                                  #Declare Variable of dictionary_file,
                                                                                           #and open the dictionary.txt file,
                                                                                           #using argument 'r' to read it

passwords = dictionary.readlines()                                                         #Declare variable passwords to read each
                                                                                           #line of the password_file (dictionary.txt file)

dictionary.close()

passwords = [item.rstrip('\n') for item in passwords]                                      #Set passwords to be an array containing all items in dictionary file

results = open('Password_result.txt', 'w')

password_found = 'false'

for password in passwords:
	if(password_found == 'false' ):
		print(password)
		try:
			wb = openedDoc.Documents.Open(filename, False, False, None, password)		
			print("\n The Password has been identified.\n Password is: "+password)  #If the password is correct, it will print the following to the
                                                                                                #screen and send the value of password to the variable "result",
                                                                                                #which will write this to the password_result.txt file
			results.write(password)
			results.close()
			password_found = 'true'
		except:
			print("This didn't work !")
			pass
	else:
		sys.exit(0)
