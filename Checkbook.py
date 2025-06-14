import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import customtkinter
import os
import string, csv

class Checkbook_Window(tk.Tk):
    def __init__(self, title):
        # setup
        super().__init__()
        self.title(title)
        self.geometry("1000x450")
        self.minsize(1000,450)

        # widgets
        self.menu = Core_Window(self)

        # run
        self.mainloop()
    
class Core_Window(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # Setup information
        xAxis = ["Flag", "Number", "Information", "Date", "Status", "Amount", "Deposit", "Balance"]
        
        # buttons 
        AddButton = tk.Button(self, text="Add Row", command = self.rowAdd)
        SaveButton = tk.Button(self, text="Save", command = self.saveApp)
        Menu = ListFrame(self, "x", 2)

        # Creates grid
        self.columnconfigure((0,1,2,3,4,5,6,7,8), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # Places Widgest
        for x in xAxis:
            text = tk.Label(self, text = x, width=15, background = "white")
            text.grid(row = 0, column = xAxis.index(x))
        Menu.grid(column = 0, row = 1, rowspan=3)
        AddButton.grid(column=1, row = 4)
        SaveButton.grid(column=2, row = 4)
    
    def rowAdd():
        setting+=1
        return
    def saveApp():
        '''
        try:
            f = open("savefile.txt", "x")
        except:
            print("file already made")
        else:
            print("file created")
            
        with open("savefile.txt", "a") as f:
            for key, value in cells.items():
                f.write(f"{key} : {value.get()}\n")
        '''
        return

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master = parent)
        self.pack(expand = True, fill = "both")

        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        self.canvas = tk.Canvas(self, background = "white")
        self.canvas.pack(expand = True, fill = "both")


title = "F.A.F.C"
Checkbook_Window(title)

'''
setting = 12
xAxis = ["Flag", "Number", "Information", "Date", "Status", "Amount", "Deposit", "Balance"]
yAxis = range(0,setting)

cells = {}

title = "FAFC"
mainwindow.title(title)

for y in yAxis:
    label = Label(mainwindow, text = y+1, width = 5, background = "white")
    label.grid(row=y+1, column=0)


for x in xAxis:
    label = Label(mainwindow, text = x, width = 15, background = "white")
    label.grid(row = 0, column = xAxis.index(x) + 1, sticky = "n")

for y in yAxis:
    xcoor=0
    for x in xAxis:
        id = f"{x}{y}"
        var = StringVar(mainwindow, "" ,id)
        entryCell = Entry(mainwindow, textvariable=var, width=18)
        entryCell.grid(row=y+1, column=xcoor+1)
        cells[id] = var
        xcoor+=1

def rowAdd():
    setting+=1
    return

def saveApp():
    try:
        f = open("savefile.txt", "x")
    except:
        print("file already made")
    else:
        print("file created")
        
    with open("savefile.txt", "a") as f:
        for key, value in cells.items():
            f.write(f"{key} : {value.get()}\n")
    return

submitButton = Button(mainwindow, text="Add Row", command = rowAdd)
submitButton.grid(column=1, row = setting+2)

saveButton = Button(mainwindow, text="Save", command = saveApp)
saveButton.grid(column=2, row = setting+2)


'''



