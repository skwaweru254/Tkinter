#! /usr/bin/python
import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time

# connecting to the database
db = mysql.connector.connect(host="localhost", user="root", passwd="Jan4th2022#", database="simon",auth_plugin='mysql_native_password')
mycur = db.cursor()

gui = tkinter.Tk()

# You app widgets will go here, object too

# Adding a label widget

label = tkinter.Label(gui, text="")


# Define a function to show the popup message
def msg():
    messagebox.showinfo("Button-Message", "Hey There! I hope you are here too.")


# Configure new tkinter window

def new_window():
    newgui = Toplevel(gui)

    newgui.title("We are now brown")

    newgui.configure(background="brown")

    newgui.geometry("400x300")

    bt = tkinter.Button(newgui, text="THREE", bg="white", fg="black", command=white_window)
    bt.place(relx=0.5, rely=0.1, anchor='center')


def white_window():
    whitegui = Toplevel(gui)

    whitegui.title("We are now white")

    whitegui.configure(background="white")

    whitegui.geometry("400x300")

    bt = tkinter.Button(whitegui, text="FOUR", bg="black", fg="white", command=black_window)
    bt.place(relx=0.5, rely=0.1, anchor='center')


def black_window():
    blackgui = Toplevel(gui)

    blackgui.title("We are now black")

    blackgui.configure(background="black")

    blackgui.geometry("400x300")

    bt = tkinter.Button(blackgui, text="FOUR", bg="white", fg="red", command=register_window)
    bt.place(relx=0.5, rely=0.1, anchor='center')

def success():
    messagebox.showinfo("You have registered successfully!")

def register_window():
    register = Toplevel(gui)

    register.title("Registration")

    global username
    global password

    username = StringVar()

    password = StringVar()
    
    Label(register, text= "Register an account",bg="white",fg= "black", font="bold", width=500).place(relx=0.5, rely=0.2, anchor='center')
    
    Label(register, text="username", font="bold").place(relx=0.3, rely=0.3, anchor='e')
    
    Entry(register, textvariable=username).place(relx=0.5, rely=0.3, anchor='center')

    Label(register, text="password", font="bold").place(relx=0.3, rely=0.4, anchor='e')

    Entry(register, textvariable=password).place(relx=0.5, rely=0.4, anchor='center')


    register.configure(background="white")

    register.geometry("400x300")

    bt = tkinter.Button(register_window, text="FOUR", bg="white", fg="red", command=success)
    bt.place(relx=0.5, rely=0.1, anchor='center')


# Button to navigate to new window

bt = tkinter.Button(gui, text="TWO", bg="white", fg="black", command=new_window)
bt.place(relx=0.5, rely=0.1, anchor='center')

# Adding a button widget

bt = tkinter.Button(gui, text="Entered", bg="yellow", fg="black", command=msg)
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
