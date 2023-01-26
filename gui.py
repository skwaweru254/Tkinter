#! /usr/bin/python

import tkinter

gui = tkinter.Tk()

# You app widgets will go here, object too

# Adding a label widget

label = tkinter.Label(gui, text = "")

# Adding a button widget

bt = tkinter.Button (gui, text="Entered", bg="yellow", fg="black")
bt.grid (column=1, row=0)

# Gui title

gui.title("We are here - Tkinter")

# Configure background color

gui.configure(background="orange")

# Set window size

gui.geometry('500x400')


# Event mainloop method

gui.mainloop()