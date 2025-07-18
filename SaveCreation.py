import tkinter as tk
from tkinter import ttk
import json
import os

#This section of python creates the login menu.
class Account_Creation(tk.Tk):
    def Go(self):
        # main setup
        self.title("F.A.F.C.")
        self.geometry("400x100")
        self.minsize(400,100)

        # widgets
        self.menu = Menu(self)
        self.mainloop()
        return self.menu.FileName, self.menu.Password

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.filename = 0
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.FileName = ""
        self.Password = ""
        self.create_widgets()

    def create_widgets(self):
        # creates widgets
        TitleLable = tk.Label(self,text=(f"Enter the Name for the Account:"), font=("Times New Roman",10))
        self.TitleEntry = tk.Entry(self, width=25, font=("Times New Roman",10))
        PasswordLable = tk.Label(self, text="  Enter the Password:", font=("Times New Roman",10))
        self.PasswordEntry = tk.Entry(self, width=25, font=("Times New Roman",10))
        SubmitButton = tk.Button(self, text="Submit", font=("Times New Roman",10), command=self.submit_click)

        # creates grid
        self.columnconfigure((0,1,2,3,4), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2), weight = 1, uniform = "a")

        # place widgets
        TitleLable.grid(row=0, column=0, columnspan=3)
        self.TitleEntry.grid(row=0, column=3, columnspan=3)
        PasswordLable.grid(row=1, column=0, columnspan=2)
        self.PasswordEntry.grid(row=1, column=3, columnspan=3)
        SubmitButton.grid(row=2, column=0, columnspan=5)

    def submit_click(self):
        self.FileName = self.TitleEntry.get()
        self.Password = self.PasswordEntry.get()
        f = open(f"SaveData\{self.FileName}.txt", 'x')
        for x in range(0,20):
            row = ["", "", "", "", "", "", ""]
            f.write(f"{json.dumps(row)}\n")
        f.close()

        self.quit()
        self.destroy()

if __name__=="__main__":
    Account_Creation().Go()