import tkinter as tk
from tkinter import ttk
import os

#This section of python creates the login menu.
class Password_Entry(tk.Tk):
    def Go(self, picked):
        # main setup
        self.title("F.A.F.C.")
        self.geometry("250x100")
        self.minsize(250,100)

        # widgets
        self.menu = Menu(self, picked)
        self.mainloop()
        self.destroy()
        return self.menu.typed_password

class Menu(ttk.Frame):
    def __init__(self, parent, picked):
        super().__init__(parent)
        self.filename = picked
        self.place(x=0, y=0, relwidth=1, relheight=1)
        self.typed_password = ""
        self.create_widgets()

    def create_widgets(self):
        # creates widgets
        TitleLable = tk.Label(self,text=(f"Enter the Password for: {self.filename}"), font=("Times New Roman",12))
        PasswordLable = tk.Label(self, text="Password: ", font=("Times New Roman",10))
        self.PasswordEntry = tk.Entry(self, width=25, font=("Times New Roman",10))
        
        SubmitButton = tk.Button(self, text="Submit", font=("Times New Roman",10), command=self.submit_click)

        # creates grid
        self.columnconfigure((0,1,2), weight = 1, uniform = "a")
        self.rowconfigure((0,1,2), weight = 1, uniform = "a")

        # place widgets
        TitleLable.grid(row=0, column=0, columnspan=3)
        PasswordLable.grid(row=1, column=0)
        self.PasswordEntry.grid(row=1, column=1, columnspan=2)
        SubmitButton.grid(row=2, column=0, columnspan=3)

    def submit_click(self):
        self.typed_password = self.PasswordEntry.get()
        self.quit()
        self.destroy()

if __name__=="__main__":
    Password_Entry().Go()