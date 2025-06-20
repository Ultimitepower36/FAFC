import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import string, csv

class Checkbook_Window(tk.Tk):
    def __init__(self, title):
        # setup
        super().__init__()
        self.title(title)
        self.geometry("900x450")
        self.minsize(900,450)
        self.maxsize(900,450)
        
        # Temp Values
        data = [("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory"),("Megan","Sorro"), ("Charlie", "Gregory")]

        # widgets
        self.menu = Core_Window(self, data)
        self.check = ListFrame(self, data , 25)

        # run
        self.mainloop()
    
class Core_Window(ttk.Frame):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=0.3)
        self.create_widgets(data)

    def create_widgets(self, data):
        # Setup information
        xAxis = ["Number", "Flag", "Information", "Date", "Status", "Amount", "Deposit", "Balance"]
        
        # buttons/labels
        FileName = tk.Label(self, text = "input", background = "white" )
        AddButton = tk.Button(self, text="Add Row", command = self.rowAdd)
        SaveButton = tk.Button(self, text="Save", command = self.saveApp(data))

        # Creates grid
        self.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3), weight = 1, uniform = "a")

        # Places Widgest
        FileName.grid(row = 0, column = 0)
        for x in xAxis:
            text = tk.Label(self, text = x, width=15, background = "white")
            text.grid(row = 2, column = xAxis.index(x))
        AddButton.grid(column=0, row = 1)
        SaveButton.grid(column=1, row = 1)
    
    def rowAdd():
        
        return
    def saveApp(self, data):
        try:
            f = open("savefile.txt", "x")
        except:
            print("file already made")
        else:
            print("file created")
            
        with open("savefile.txt", "a") as f:
            f = open("savefile.txt", 'r+')
            f.truncate(0)
            for series in data:
                f.write(f"{series}\n")
        return

class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master = parent)
        self.place(x=0, y=90, relwidth=1, relheight=0.78)

        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        self.canvas = tk.Canvas(self, background = "white", scrollregion = (0,0,900,self.list_height))
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # display frame
        self.frame = ttk.Frame(self)
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand = True, fill = 'both', pady = 1, padx=5)

        # scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        self.scrollbar.place(relx=1, rely=0, relheight = 1, anchor = 'ne')


        #events
        self.canvas.bind_all('<MouseWheel>', lambda event: self.canvas.yview_scroll(-int(event.delta / 60),"units"))
        self.bind('<Configure>', self.update_size)


    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            xheight = self.list_height
        else:
            xheight = self.winfo_height
            self.canvas.unbind_all('<MouseWheel>')
        self.canvas.create_window((0,0), window = self.frame, anchor = "nw", width = 900, height = xheight)


    def create_item(self, index, item):
        frame = tk.Frame(self.frame)
        index +=1

        # Grid layout
        frame.rowconfigure(0, weight = 1)
        frame.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform='a')

        #widgets
        tk.Label(frame, text = f'{index}', width=111, background = "white").grid(row=0, column=0)
        z=1
        for entry in item:
            var = tk.StringVar(value=entry)
            tk.Entry(frame, textvariable=var, width=111, background = "white").grid(row=0, column=z)
            z+=1

        return frame

        

title = "F.A.F.C"
Checkbook_Window(title)

