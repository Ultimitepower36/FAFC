import tkinter as tk
from tkinter import filedialog
import os

def open_folder_dialog():
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if folder_path:
        display_folder_contents(folder_path)

def display_folder_contents(folder_path):
    try:
        folder_contents = os.listdir(folder_path)
        listbox.delete(0, tk.END)  # Clear the current list

        for item in folder_contents:
            listbox.insert(tk.END, item)

    except Exception as e:
        listbox.delete(0, tk.END)  # Clear the current list
        listbox.insert(tk.END, f"Error: {str(e)}")

def listboxSelection(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    #Open Checkbook with selected file here

parent = tk.Tk()
parent.title("Free Anchored Financial Checkbook")

open_button = tk.Button(parent, text="Open Folder", font=("Times New Roman", 10), command=open_folder_dialog)
open_button.pack(padx=20, pady=20)
listbox = tk.Listbox(parent, height=15, width=40)
listbox.pack(padx=20, pady=20)

SubmitButton = tk.Button(parent, text="Open Checkbook", font=("Times New Roman",10), command=listboxSelection)
SubmitButton.pack(padx=20, pady=20)
NewFileButton = tk.Button(parent, text="Make New Checkbook", font=("Times New Roman",10))
NewFileButton.pack(padx=20, pady=20)


parent.mainloop()