import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

import Password
import SaveCreation
import Checkbook

class Opening_Window(tk.Tk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("Free Anchored Financial Checkbook")
        self.minsize(400,300)

        # widgets
        self.menu = Menu(self)
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # Creates widgets
        self.open_button = tk.Button(self, text="Open Folder", font=("Times New Roman", 10), command=self.open_folder_dialog)
        self.listbox = tk.Listbox(self, width=50)
        self.submit_button = tk.Button(self, text="Open Checkbook", font=("Times New Roman",10), command=self.listboxSelection)
        self.NewFile_button = tk.Button(self, text="Make New Checkbook", font=("Times New Roman",10), command=self.openBox_SaveCreation)
        
        # Creates grid
        self.columnconfigure((0,1,2,3), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # Place widgets
        self.open_button.grid(row = 0, column = 0, columnspan = 4)
        self.listbox.grid(row = 1, column = 0, columnspan = 4, rowspan = 3)
        self.submit_button.grid(row = 4, column = 0, columnspan = 2)
        self.NewFile_button.grid(row = 4, column = 2, columnspan = 2)
    
    def open_folder_dialog(self):
        # Gets the file path for the save states
        self.folder_path = filedialog.askdirectory(title="Select a Folder")
        if self.folder_path:
            self.display_folder_contents(self.folder_path)

    def display_folder_contents(self, folder_path):
        # Checks the files in the path and displays them
        try:
            folder_contents = os.listdir(folder_path)
            self.listbox.delete(0, tk.END)  # Clear the current list

            for item in folder_contents:
                self.listbox.insert(tk.END, item)

        except Exception as e:
            self.listbox.delete(0, tk.END)  # Clear the current list
            self.listbox.insert(tk.END, f"Error: {str(e)}")


    def openBox_SaveCreation(self):
        t = SaveCreation.Account_Creation().Go()
        picked = t[0]
        sub_password = t[1]
        self.folder_path = "SaveData"
        Checkbook.Checkbook_Window(picked, sub_password, self.folder_path)


    def listboxSelection(self):
        # Allows for a file to be selected and moved to the next part
        widget = self.listbox
        selection=widget.curselection()
        picked = widget.get(selection[0])
        
        t = Password.Password_Entry()
        sub_password = t.Go(picked)
    
        Checkbook.Checkbook_Window(picked, sub_password, self.folder_path)
        #Open Checkbook with selected file here
        #self.openBox_Password(self, picked)


if __name__=="__main__":
    # starts program
    Opening_Window()
    
