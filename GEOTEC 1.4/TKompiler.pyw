import py_compile
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil

#initializations
surface = tk.Tk()
surface.geometry("450x240")
surface.title("TKompiler")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#about window
def aboot():
    messagebox.showinfo("About", "made by UPGSOFTWARE a division of WIZARD STUDIOS, copyleft MMXXIV, some rights reserved")

#help window
def helpmuh():
    helptext = """Open: opens a .py or .pyw file and compiles it to a .pyc file
Rename: renames a .pyc file to whatever is in the entry box
Convert: turns a .py into a .pyw file and names it whatever is in the entry box
Copy: copies a file and names it whatever is in the entry box
If you cannot find a file you compiled, look in a folder called __pycache__ in the directory of the .py file you compiled"""
    
    messagebox.showinfo("Help", helptext)

#compilation file opener
def fileopener():
    global status
    thing = filedialog.askopenfilename(filetypes = [("Python Files", "*.py"), ("Weird Python Files", "*.pyw")])
    py_compile.compile(thing)
    status.set("compiled file successfully")
    print("compiled: " + thing)

#renaming file opener
def otehrfileopener():
    global status
    rnt = t3xtvar.get()
    thing = filedialog.askopenfilename(filetypes = [("Compiled Python Files", "*.pyc")])
    os.rename(thing, rnt + ".pyc")
    status.set("renamed file successfully")
    print("renamed " + thing + "to " + rnt)

def pywunction():
    global status
    rnt = Pywow.get()
    thing = filedialog.askopenfilename(filetypes = [("Python Files", "*.py")])
    os.rename(thing, rnt + ".pyw")
    status.set("renamed file successfully")
    print("renamed " + thing + "to " + rnt)

def copunction():
    global status
    rnt = copything.get()
    thing = filedialog.askopenfilename(filetypes = [("Python Files", "*.py"), ("Compiled Python Files", "*.pyc"), ("Weird Python Files", "*.pyw")])
    shutil.copy(thing, rnt)
    status.set("Copied file successfully")
    print("renamed " + thing + "to " + rnt)

#random variables
t3xtvar = tk.StringVar()
status = tk.StringVar()
Pywow = tk.StringVar()
copything = tk.StringVar()

#menubar
menubar = tk.Menu(surface)
#file
file = tk.Menu(menubar, tearoff = 0) 
file.add_command(label = "Quit", command = exit)
menubar.add_cascade(label = "File", menu = file)
#help
help = tk.Menu(menubar, tearoff = 0)
help.add_command(label = "About", command = aboot)
help.add_command(label = "Help", command = helpmuh)
menubar.add_cascade(label = "Help", menu = help)
surface.configure(menu = menubar)

#carne y papas
Mainframe = tk.Frame(surface)
#title thing
toplabel = tk.Label(Mainframe, text = "TKompiler", font = 25).grid(row = 0, column = 0, columnspan = 3)
#opener button
filebutton = ttk.Button(Mainframe, text = "Compile python source files to .pyc", command = fileopener).grid(row = 1, column = 0, columnspan = 3, pady = 10)
#renaming things
rename = ttk.Button(Mainframe, text = "Rename", command = otehrfileopener).grid(row = 3, column = 2)
rntextlabel = tk.Label(Mainframe, text = "Rename .pyc:").grid(row = 3, column = 0)
renametext = ttk.Entry(Mainframe, textvariable = t3xtvar).grid(row = 3, column = 1)
#to pyw
pywlabel = tk.Label(Mainframe, text = "Convert py to pyw:").grid(row = 4, column = 0)
pywtext = tk.Entry(Mainframe, textvariable = Pywow).grid(row = 4, column = 1)
pywutton = ttk.Button(Mainframe, text = "Convert", command = pywunction).grid(row = 4, column = 2)
#copy
copylabel = tk.Label(Mainframe, text = "Copy file INCLUDE EXTENTION:").grid(row = 5, column = 0)
copytext = tk.Entry(Mainframe, textvariable = copything).grid(row = 5, column = 1)
coputton = ttk.Button(Mainframe, text = "Copy", command = copunction).grid(row = 5, column = 2)
#status
statuslabel = tk.Label(Mainframe, text = "Status should be here", textvariable = status).grid(row = 6, column = 0, columnspan = 3)
Mainframe.pack()

surface.mainloop()