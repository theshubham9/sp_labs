while True:
    print("Enter 1 for string.")
    print("Enter 2 for file.\n")
    a = input("Enter you choice: ")
    if a == '1':
        import sys
        import hashlib
        s = input("Enter the string: ")
        s = s.encode("utf-8")
        h = hashlib.new("sha1")
        h.update(s)
        h.hexdigest()
        print("SHA-1: ",h.hexdigest(),"\n")

        h = hashlib.new("sha256")
        h.update(s)
        h.hexdigest()
        print("SHA-256: ",h.hexdigest(),"\n")

        h = hashlib.new("sha512")
        h.update(s)
        h.hexdigest()
        print("SHA-512: ",h.hexdigest(),"\n")
        '''
        if sys.version_info < (3, 6): import sha3
        h = hashlib
        h.update(a)
        h.hexdigest()
        print("SHA-3: ",h.hexdigest(),"\n")
        '''
        break
    
    elif a == '2':
        import sys
        import hashlib
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        root.update()
        root.fileName = filedialog.askopenfilename()
        print(root.fileName, "\n")
        h = hashlib.sha1()
        with open(root.fileName, 'rb') as afile:
            buf = afile.read()
            h.update(buf)
        h.hexdigest()
        print("SHA-1: ",h.hexdigest(),"\n")

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
        print("\n***Invalid choice.\n")
        continue
