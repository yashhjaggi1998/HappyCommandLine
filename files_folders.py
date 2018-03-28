import os,subprocess,sys
from tkinter import *

ff = Tk()
ff.minsize(600,600)
ff.title("Files/Folders")

def create_file():
	filename = e1.get()
	subprocess.call(['touch',filename])

def delete_file():
	filename = e2.get()
	subprocess.call(['rm',filename])

def edit_file():   #still work to be done 
	filename = e3.get()
	subprocess.call(['nano',filename])

def display_file():
	print(e4.get())   #put a list box here

def file_permission():   #input format filename<space>permission(777)
	filename = e5.get()
	filename = filename.split(" ")
	subprocess.call(['chmod' , filename[0] , filename[1]])

def copy_file(): # format filename<space>sourcedir<space>destdir
	input = e6.get()
	input = input.split(" ")
	filename = input[0]
	source = input[1]
	destination = input[2]
	source = source + "/" + filename
	subprocess.call(['cp', source , destination])

def move_file():   # format filename<space>sourcedir<space>destdir
	input = e7.get()
	input = input.split(" ")
	filename = input[0]
	source = input[1]
	destination = input[2]
	source = source + "/" + filename
	subprocess.call(['mv', source , destination])

def create_folder():
	foldername = e8.get()
	subprocess.call(['mkdir' , foldername])

def delete_folder():
	foldername = e9.get()
	subprocess.call(['rmdir' , foldername])

def list_folder():
	foldername = e10.get()
	subprocess.call(['ls','-l',foldername])




e1 = Entry(ff)
e1.grid(row = 0 , column = 1)
Button(ff,text="Create a New File" , command = create_file).grid(row = 0)   #  $cat > filename 

e2 = Entry(ff)
e2.grid(row = 1 , column = 1)
deletefile = Button(ff,text="Delete an Existing File", command = delete_file).grid(row = 1)   # $rm filename

e3 = Entry(ff)
e3.grid(row = 2 , column = 1)
editfile = Button(ff,text="Edit a file", command = edit_file).grid(row = 2)    # $ nano filename    => to be installed

e4 = Entry(ff)
e4.grid(row = 3 , column = 1)
displayfile = Button(ff,text="Display Contents of a file", command = display_file).grid(row = 3)    #cat

v = StringVar(ff, value = "filename<space>permission")
e5 = Entry(ff, width = 30 , textvariable = v)

# e5.insert(END , 'default text')  => works
e5.grid(row = 4 , column = 1)
filepermission = Button(ff,text="Change File permissions", command = file_permission).grid(row = 4)   #chmod

e6 = Entry(ff)
e6.grid(row = 5 , column = 1)
copyfile = Button(ff,text="Copy a file to new destination", command = copy_file).grid(row = 5)   # cp

e7 = Entry(ff)
e7.grid(row = 6 , column = 1)
movefile = Button(ff,text="Move a file to new destination", command = move_file).grid(row = 6)

e8 = Entry(ff)
e8.grid(row = 7 , column = 1)
createfolder = Button(ff,text="Create a New Folder", command = create_folder).grid(row = 7)

e9 = Entry(ff)
e9.grid(row = 8 , column = 1)
deletefolder = Button(ff,text="Delete an Existing Folder", command = delete_folder).grid(row = 8)

e10 = Entry(ff)
e10.grid(row = 9 , column = 1)
listfolder = Button(ff,text="List contents of current folder", command = list_folder).grid(row = 9)



ff.mainloop()				