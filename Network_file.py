import os,sys
import subprocess
from tkinter import * 

net = Tk()
net.minsize(800,800)
net.title("Networking")


def ifconfig():
	print(e1.get())

def downloadfile():
	print(e2.get())

def edit_file():
	print(e3.get())

def display_file():
	print(e4.get())

def file_permission():
	print(e5.get())

def copy_file():
	print(e6.get())

def move_file():
	print(e7.get())

def create_folder():
	print(e8.get())

def delete_folder():
	print(e9.get())

def list_folder():
	print(e10.get())


e1 = Entry(ff)
e1.grid(row = 0 , column = 1)
Button(net, text='Network interfaces' , command = ifconfig)  #   $ifconfig

e2 = Entry(ff)
e2.grid(row = 0 , column = 1)
Button(net, text='Download A File' , command = downloadfile)   #    $wget urk

e3 = Entry(ff)
e3.grid(row = 0 , column = 1)
Button(net, text='Get Information About Domain' , command = domaininfo)   #     $whois ip   => to be installed externally. Create a shell file for all things to be installed

e4 = Entry(ff)
e4.grid(row = 0 , column = 1)
Button(net, text='Ping to Check Internet Connection' , command = ping)     # ping ip

e5 = Entry(ff)
e5.grid(row = 0 , column = 1)
Button(net, text='Display HostName' , command = displayhostname)     # $ hostname

e6 = Entry(ff)
e6.grid(row = 0 , column = 1)
Button(net, text='Change HostName' , command = changehostname)     # $ sudo hostname new-hostname

e7 = Entry(ff)
e7.grid(row = 0 , column = 1)
Button(net, text='Trace the path that a packet takes to its destination' , command = traceroute)     # $ traceroute ip   => to be installed

e8 = Entry(ff)
e8.grid(row = 0 , column = 1)
Button(net, text='Telnet Connection' , command = telnet)     # $ telnet ip port

e9 = Entry(ff)
e9.grid(row = 0 , column = 1)
Button(net, text='DNS lookup and display server answer' , command = dig)     # $ dig ip

e10 = Entry(ff)
e10.grid(row = 0 , column = 1)
Button(net, text='Release ip and get a new one from DHCP' , command = dhclient)     # $ dhclient -r

e11 = Entry(ff)
e11.grid(row = 0 , column = 1)
Button(net, text='List Open Sockets' , command = netstat)     # $ netstat -l

net.mainloop()
