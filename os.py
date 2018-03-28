import os,sys,subprocess
from tkinter import * 

root = Tk()
root.minsize(600,600)
root.title("Happy system Command Lining :)")


#portion of window used to display current working directory
label = Label(root, text="Current Working Directory")  # Displays the name
label.pack()
curr_dir_display = Listbox(root, bg = 'blue' , bd = 4 , fg = 'white' , height = 1 , width = 50)
curr_dir_display.pack(padx = 8 , pady = 6 )
curr_dir_display.insert(0,os.getcwd())

Network = Button(root, text='Networking')
Network.pack()

Permission = Button(root, text='Permissions')
Permission.pack()

FolderOrFile = Button(root, text='Files/Folder')
FolderOrFile.pack()

SysInfo = Button(root, text='System Information')
SysInfo.pack()

SysControl = Button(root, text='System Control')
SysControl.pack()

Search = Button(root, text='Search/Find')
Search.pack()

Media = Button(root, text='Media')
Media.pack()

PackManager = Button(root, text='Package Manager')
PackManager.pack()

Hacking = Button(root, text='Hacking Tools')
Hacking.pack()

TerminalGames = Button(root, text='Terminal Games')
TerminalGames.pack()

CompileAndExecute = Button(root, text='Compile And Execute')
CompileAndExecute.pack()

def network(event):
	import Network_file

def permission(event):
	p = Tk()
	p.minsize(600,600)
	p.title("Permissions")
	p.mainloop()

def folderorfile(event):
	import files_folders
	
def sysinfo(event):
	si = Tk()
	si.minsize(600,600)
	si.title("System Information")
	si.mainloop()

def syscontrol(event):
	sc = Tk()
	sc.minsize(600,600)
	sc.title("System Control")
	sc.mainloop()

def search(event):
	s = Tk()
	s.minsize(600,600)
	s.title("Search And Find")
	s.mainloop()

def media(event):
	m = Tk()
	m.minsize(600,600)
	m.title("Search And Find")
	m.mainloop()

def packmanager(event):
	pm = Tk()
	pm.minsize(600,600)
	pm.title("Search And Find")
	pm.mainloop()

def hacking(event):
	h = Tk()
	h.minsize(600,600)
	h.title("Search And Find")
	h.mainloop()

def compileandexecute(event):
	ce = Tk()
	ce.minsize(200,200)
	ce.title("Compile And Execute")

	listbox = Listbox(ce,bg = 'blue' , bd = 4 , fg = 'white')
	listbox.pack(padx = 10 , pady = 10)
	filename = "tr.cpp"
	temp = "g++ " + filename 
	a = os.system(temp)
	if(a == 0):
		proc1 = subprocess.Popen(["./a.out"], stdout=subprocess.PIPE, shell=True)
		(out1, err1) = proc1.communicate()
		listbox.insert(0,out1)
	else:
		listbox.insert(0,"No such file exists")
	ce.mainloop()


Network.bind('<Button-1>', network)
Permission.bind('<Button-1>', permission)
FolderOrFile.bind('<Button-1>', folderorfile)
SysInfo.bind('<Button-1>', sysinfo)
SysControl.bind('<Button-1>', syscontrol)
Search.bind('<Button-1>', search)
Media.bind('<Button-1>', media)
PackManager.bind('<Button-1>', packmanager)
Hacking.bind('<Button-1>', hacking)
CompileAndExecute.bind('<Button-1>', compileandexecute)
root.mainloop()