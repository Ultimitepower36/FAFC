from tkinter import *
import string, csv


setting = 12
xAxis = ["Flag", "Number", "Information", "Date", "Status", "Amount", "Deposit", "Balance"]
yAxis = range(0,setting)

cells = {}

mainwindow = Tk()

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

mainwindow.mainloop()
