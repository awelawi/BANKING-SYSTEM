from cgitb import text
from glob import glob
import math
from tkinter import*
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#the buttons assume the position of its parent

def ButtonClick(number):
    # e.delete(0, END)
    current_num = e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))

def ButtonClear():
    "Clears the text box"
    e.delete(0, END)


def ButtonAdd():
    
    "Adds the values in the text box"
    first_num = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    e.delete(0, END)

def ButtonEqual():
    "Equator function"
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def ButtonDivide():
    first_num = e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_num)
    e.delete(0, END)

def ButtonMult():
    first_num = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_num)
    e.delete(0, END)

def ButtonSub():
    first_num = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_num)
    e.delete(0, END)




#Define the buttins
button1 = Button(root, text="1", padx=40, pady=20, command = lambda:ButtonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda:ButtonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda:ButtonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda:ButtonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:ButtonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda:ButtonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda:ButtonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:ButtonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda:ButtonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda:ButtonClick(0))
button_add = Button(root, text="+", padx=39, pady=20,command= ButtonAdd)
button_equal = Button(root, text="=", padx=91, pady=20,command=ButtonEqual)
button_clear = Button(root, text="Clear", padx=79, pady=20,command=ButtonClear)

button_subtract = Button(root, text="-", padx=41, pady=20,command=ButtonSub)
button_multiply = Button(root, text="*", padx=40, pady=20,command=ButtonMult)
button_divide = Button(root, text="/", padx=41, pady=20,command=ButtonDivide)

# Put the button on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

button0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=3)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_multiply.grid(row=6, column=2)

root.mainloop()