while True:
    print("Enter 1 for string.")
    print("Enter 2 for file.\n")                        #Strings for asking the user what would they like to do
    a = input("Enter you choice: ")                     #decision making
    if a == '1':
        import sys
        import hashlib
        s = input("Enter the string: ")                 #asks user for the string
        s = s.encode("utf-8")                           #encodes the string in utf-8
        h = hashlib.new("sha1")                         #extracts the SHA-1 algorithm from hashlib
        h.update(s)                                     
        h.hexdigest()                                   #encodes the string into SHA-1
        print("SHA-1: ",h.hexdigest(),"\n")             #prints the SHA-1 string

        h = hashlib.new("sha256")                       #similarly for SHA-256
        h.update(s)
        h.hexdigest()
        print("SHA-256: ",h.hexdigest(),"\n")

        h = hashlib.new("sha512")                       #similarly for SHA-512
        h.update(s)
        h.hexdigest()
        print("SHA-512: ",h.hexdigest(),"\n")
        break
    
    elif a == '2':                                      #for hash value of a file
        import sys
        import hashlib
        import tkinter as tk                            #for using pyton's GUI
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()                                 #to close the GUI window
        root.update()                                   #update the file selection
        root.fileName = filedialog.askopenfilename()    #open dialog box for selecting the file
        print(root.fileName, "\n")                      #prints the path of the selected file
        h = hashlib.sha1()                              #same as above (for SHA-1 calculation)
        with open(root.fileName, 'rb') as afile:        #convert the filename into binary
            buf = afile.read()                          #reads that binary value
            h.update(buf)
        h.hexdigest()
        print("SHA-1: ",h.hexdigest(),"\n")             #prints the hash value

        h = hashlib.sha256()
        with open(root.fileName, 'rb') as afile:
            buf = afile.read()
            h.update(buf)
        h.hexdigest()
        print("SHA-256: ",h.hexdigest(),"\n")

        h = hashlib.sha512()
        with open(root.fileName, 'rb') as afile:
            buf = afile.read()
            h.update(buf)
        h.hexdigest()
        print("SHA-512: ",h.hexdigest(),"\n")
        break
    
    else:
        print("\n***Invalid choice.\n")                 #generates the loop again if user inputs invalid value
        continue
