import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import json

#json loaditron
os.chdir(os.path.dirname(os.path.realpath(__file__)))
tla = open(str("config.json"))
ano = json.load(tla)

#initializations
surface = tk.Tk()
surface.geometry("450x200")
surface.title("GeoTec Launcher")

#important application variables
nfilename = tk.StringVar()
status = tk.StringVar()
current = tk.StringVar()
changegravity = tk.StringVar()
editedit = tk.StringVar()
if ano[1] == False:
    changegravity.set("enable gravity (expect bugs)")
else:
    changegravity.set("disable gravity")
current.set(f"Current savefile: {ano[0]}")
gravitron = ano[1]
if ano[2] == True:
    editedit.set("Disable Edit Mode")
else:
    editedit.set("Enable Edit Mode")

#temlate
geometry = {
    "basic": {
        "x": [],
        "y": [],
        "w": 50,
        "h": 50,
        "tags": [],
        "color": [255, 255, 255],
        "texture": None,
        "collision": True,
    },
}

portals = {
    "basic": {
        "x1": [],
        "y1": [],
        "x2": [],
        "y2": [],
        "w": 50,
        "h": 50,
        "tags": [],
        "color": [0, 0, 255],
        "texture": None,
    }
}

text = {
    "TESTIFICATE": {
        "words": "THIS IS NOT A DRILL, IT IS A TEST",
        "x": [],
        "y": [],
        "tags": [],
        "isgui": False,
        "bkground_color": [255, 0, 255],
        "clickable": False
    }
}

def launch():
    os.system("python Project_Modularity.py")

def new():
    walker = nfilename.get()
    os.system(f"mkdir {walker}")
    os.chdir(f"{walker}")
    os.system("cd . > modularity.json")
    os.system("cd . > portals.json")
    with open("modularity.json", "w") as module:
        json.dump(geometry, module, indent=4)
        module.close()
    with open("portals.json", "w") as cakeislie:
        json.dump(portals, cakeislie, indent=4)
        cakeislie.close()
    with open("text.json", "w") as msnmsnger:
        json.dump(text, msnmsnger, indent=4)
        msnmsnger.close()
    os.chdir("C:/Users/somer/OneDrive/Documents/programming/python/GEOTEC 1.4")
    status.set("New savefile created")

def selectfolder():
    global gravitron
    global ano
    bob = filedialog.askdirectory()
    settinglist = [bob, gravitron, ano[2]]
    print(bob)
    with open("config.json", "w") as bobulous:
        json.dump(settinglist, bobulous, indent=4)
        bobulous.close()
    status.set("Savefile selected")
    tla = open(str("config.json"))
    ano = json.load(tla)
    current.set(f"Current savefile: {ano[0]}")

def aboot():
    messagebox.showinfo("About", "made by UPGSOFTWARE a division of WIZARD STUDIOS, copyleft MMXXIV, some rights reserved")

def oot():
    messagebox.showinfo("Selected Save", current.get())

def chanGe():
    global gravitron
    if gravitron == False:
        gravitron = True
        changegravity.set("disable gravity")
        status.set("gravity enabled")
    else:
        gravitron = False
        changegravity.set("enable gravity (expect bugs)")
        status.set("gravity disabled")
    settinglist = [ano[0], gravitron, ano[2]]
    with open("config.json", "w") as bobulous:
        json.dump(settinglist, bobulous, indent=4)
        bobulous.close()

def Eddaculious():
    global gravitron

    if ano[2] == False:
        ano[2] = True
        editedit.set("Disable Edit Mode")
        status.set("Edit Mode Enabled")
    else:
        ano[2] = False
        editedit.set("Enable Edit Mode")
        status.set("Edit Mode Disabled")

    settinglist = [ano[0], gravitron, ano[2]]

    with open("config.json", "w") as bobulous:
        json.dump(settinglist, bobulous, indent=4)
        bobulous.close()

#menubar
menubar = tk.Menu(surface)
#file
file = tk.Menu(menubar, tearoff = 0) 
file.add_command(label = "Quit", command = exit)
menubar.add_cascade(label = "File", menu = file)
#view
view = tk.Menu(menubar, tearoff=0)
view.add_command(label="Selected Savefile", command=oot)
menubar.add_cascade(label="View", menu=view)
#help
helpmuh = tk.Menu(menubar, tearoff=0)
helpmuh.add_command(label="About", command=aboot)
menubar.add_cascade(label="Help", menu=helpmuh)
surface.configure(menu = menubar)

#carne y patatas
Mainframe = tk.Frame(surface)
#logo
logo = tk.Label(Mainframe, text="GeoTec Launcher", font=25).grid(row=0, column=0, columnspan=3)
#playbutton
playbutton = ttk.Button(Mainframe, text="Play", command=launch).grid(row=1, column=0, columnspan=3)
#new save file
notice = tk.Label(Mainframe, text="make sure you fill out all boxes below if you want to make a new save").grid(row=2, column=0, columnspan=3)
dirname = tk.Label(Mainframe, text="new save file name:").grid(row=3, column=0)
uinput = tk.Entry(Mainframe, textvariable=nfilename).grid(row=3, column=1)
enterbutton = ttk.Button(master=Mainframe, text="Create new save file", command=new).grid(row=3, column=2)
#choose savefile
filebutton = ttk.Button(Mainframe, text="open save file", command=selectfolder).grid(row=5, column=0, columnspan=3)
#gravitar
changebutton = ttk.Button(Mainframe, textvariable=changegravity, command=chanGe).grid(row=7, column=1, columnspan=1)
#editmode
editbutton = ttk.Button(Mainframe, textvariable=editedit, command=Eddaculious).grid(row=8, column=1, columnspan=1)
#STATUS
statulus = tk.Label(Mainframe, text="status should be here", textvariable=status).grid(row=9, column = 1)
Mainframe.pack()

surface.mainloop()