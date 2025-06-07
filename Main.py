import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

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
        # creates widgets
        self.open_button = tk.Button(self, text="Open Folder", font=("Times New Roman", 10), command=self.open_folder_dialog)
        self.listbox = tk.Listbox(self, width=50)
        self.submit_button = tk.Button(self, text="Open Checkbook", font=("Times New Roman",10), command=self.listboxSelection)
        self.NewFile_button = tk.Button(self, text="Make New Checkbook", font=("Times New Roman",10))
        
        # creates grid
        self.columnconfigure((0,1,2,3), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2,3,4), weight = 1, uniform = "a")

        # place widgets
        self.open_button.grid(row = 0, column = 0, columnspan = 4)
        self.listbox.grid(row = 1, column = 0, columnspan = 4, rowspan = 3)
        self.submit_button.grid(row = 4, column = 0, columnspan = 2)
        self.NewFile_button.grid(row = 4, column = 2, columnspan = 2)
    
    def open_folder_dialog(self):
        folder_path = filedialog.askdirectory(title="Select a Folder")
        if folder_path:
            self.display_folder_contents(folder_path)

    def display_folder_contents(self, folder_path):
        try:
            folder_contents = os.listdir(folder_path)
            self.listbox.delete(0, tk.END)  # Clear the current list

            for item in folder_contents:
                self.listbox.insert(tk.END, item)

        except Exception as e:
            self.listbox.delete(0, tk.END)  # Clear the current list
            self.listbox.insert(tk.END, f"Error: {str(e)}")

    def openBox_Password(self, picked):
        password_window = tk.Toplevel()

    def listboxSelection(self, event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection[0])
        #Open Checkbook with selected file here
        self.openBox_Password(self, picked)

    
# starts program
Opening_Window()
    
