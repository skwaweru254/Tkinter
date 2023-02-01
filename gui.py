#! /usr/bin/python

import tkinter
from tkinter import Label, Button, Toplevel, messagebox
import mysql.connector


con = mysql.connector.connect(host = "localhost", user = "simon", password = "wellidiot", database = "tkinter")
cursor = db.cursor()

gui = tkinter.Tk()

# You app widgets will go here, object too

# Adding a label widget

label = tkinter.Label(gui, text = "")

# Define a function to show the popup message
def msg():
       messagebox.showinfo("Button-Message","Hey There! I hope you are here too.")
       

# Configure new tkinter window

def new_window():

       newgui = Toplevel(gui)

       newgui.title("We are now brown")

       newgui.configure(background="brown")

       newgui.geometry("400x300")

       bt = tkinter.Button (newgui, text="THREE", bg="white", fg="black" , command=white_window)       
       bt.place(relx=0.5, rely=0.1, anchor='center')

def white_window():

       whitegui = Toplevel(gui)

       whitegui.title("We are now white")

       whitegui.configure(background="white")

       whitegui.geometry("400x300")

       bt = tkinter.Button (whitegui, text="FOUR", bg="black", fg="white" , command=black_window)       
       bt.place(relx=0.5, rely=0.1, anchor='center')

def black_window():

       blackgui = Toplevel(gui)

       blackgui.title("We are now blck")

       blackgui.configure(background="black")

       blackgui.geometry("400x300")

       bt = tkinter.Button (blackgui, text="FOUR", bg="white", fg="red" , command=None)       
       bt.place(relx=0.5, rely=0.1, anchor='center')


# Button to navigate to new window

bt = tkinter.Button (gui, text="TWO", bg="white", fg="black" , command=new_window)
bt.place(relx=0.5, rely=0.1, anchor='center')



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