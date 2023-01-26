#! /usr/bin/python

import tkinter
from tkinter import messagebox


gui = tkinter.Tk()

# You app widgets will go here, object too

# Adding a label widget

label = tkinter.Label(gui, text = "")

# Define a function to show the popup message
def msg():
       messagebox.showinfo("Button-Message","Hey There! I hope you are here too.")


# Adding a button widget

bt = tkinter.Button (gui, text="Entered", bg="yellow", fg="black" , command=msg)
bt.place(relx=0.5, rely=0.5, anchor='center')
# bt.pack(side="top")


# Gui title

gui.title("We are here - Tkinter")

# Configure background color

gui.configure(background="orange")

# Set window size

gui.geometry('500x400')


# Event mainloop method

gui.mainloop()