from tkinter import *

window = Tk()

UsernameLable = Label(window,text="Username: ").grid(row=0, column=0)
UsernameEntry = Entry(window).grid(row=0, column=1)

PasswordLable = Label(window, text="Password: ").grid(row=2, column=0)
UsernameEntry = Entry(window).grid(row=0, column=1)


window.mainloop()