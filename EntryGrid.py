from tkinter import *

#This section of python creates the login menu.

window = Tk()

TitleLable = Label(window,text="Enter your information", font=("Times New Roman",12)).grid(row=0, column=0, columnspan=2)

UsernameLable = Label(window,text="Username: ", font=("Times New Roman",10)).grid(row=1, column=0)
UsernameEntry = Entry(window, font=("Times New Roman",10)).grid(row=1, column=1)

PasswordLable = Label(window, text="Password: ", font=("Times New Roman",10)).grid(row=2, column=0)
PasswordEntry = Entry(window, font=("Times New Roman",10)).grid(row=2, column=1)

SubmitButton = Button(window, text="Submit", font=("Times New Roman",10)).grid(row=3, column=0, columnspan=2)

window.mainloop()