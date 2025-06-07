import tkinter as tk
from tkinter import ttk
import os

#This section of python creates the login menu.
class Password_Entry(tk.Tk):
    def __init__(self):
        # main setup
        super().__init__()
        self.title("F.A.F.C.")
        self.geometry("250x100")
        self.minsize(250,100)

        # widgets
        self.menu = Menu(self)
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.filename = 0
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        # creates widgets
        TitleLable = tk.Label(self,text=(f"Enter the Password for:{self.filename}"), font=("Times New Roman",12))
        PasswordLable = tk.Label(self, text="Password: ", font=("Times New Roman",10))
        PasswordEntry = tk.Entry(self, width=25, font=("Times New Roman",10))
        SubmitButton = tk.Button(self, text="Submit", font=("Times New Roman",10))

        # creates grid
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2), weight = 1, uniform = "a")

        # place widgets
        TitleLable.grid(row=0, column=0, columnspan=3)
        PasswordLable.grid(row=1, column=0)
        PasswordEntry.grid(row=1, column=1, columnspan=2)
        SubmitButton.grid(row=2, column=0, columnspan=3)

Password_Entry()