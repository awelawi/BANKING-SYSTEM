from distutils import command
from tkinter import *
root = Tk()

# Creating a label widget
# myLabel1 = Label(root, text="hello world").grid(row = 0, column=0)
# myLabel2= Label(root, text="My name is John Elder").grid(row = 1, column=0)

# Shoving it onto the screen using pack() or grid for beyyer interface
# Position is relative
# myLabel1.grid(row = 0, column=0)
# myLabel2.grid(row = 1, column=0)

#Create input fields using an ENTRY Widget
e = Entry(root, width=50, fg = "green", border=5)
e.pack()
#To create a placeholder text
e.insert(0, "enter your name: ")
# PROGRAMMING YOUR BUTTON
def myClick():
    #To get the text from the user and use it for other purposes
    hello = "hello " + e.get()
    myLabel = Label(root, text= hello , fg = "blue")
    myLabel.pack()

# Creat a button diget, use fg for foreground and bg for background you can also use hex color code for this
#to make it more unique
myButton = Button(root, text = "Enter your name", pady=200, padx=200, command=myClick, fg="yellow", bg="red")


# pack the button
myButton.pack()
# event loop for constantly running GUI
root.mainloop()