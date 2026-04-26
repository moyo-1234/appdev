import tkinter
from tkinter import*
flag = 1

root = tkinter.Tk("900x900")

def ttt1():
    global flag
    if flag == 1:
        button1.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        button1.config(text = "O")
        flag = flag + 1

def ttt2():
    global flag
    if flag == 1:
        button2.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        button2.config(text = "O")
        flag = flag + 1

def ttt3():
    global flag
    if flag == 1:
        button3.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        button3.config(text = "O")
        flag = flag + 1

def tttA():
    global flag
    if flag == 1:
        buttona.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttona.config(text = "O")
        flag = flag + 1

def tttB():
    global flag
    if flag == 1:
        buttonb.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttonb.config(text = "O")
        flag = flag + 1

def tttC():
    global flag
    if flag == 1:
        buttonc.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttonc.config(text = "O")
        flag = flag + 1

def tttX():
    global flag
    if flag == 1:
        buttonx.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttonx.config(text = "O")
        flag = flag + 1


def tttY():
    global flag
    if flag == 1:
        buttony.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttony.config(text = "O")
        flag = flag + 1


def tttZ():
    global flag
    if flag == 1:
        buttonz.config(text = "X")
        flag = flag - 1
    elif flag == 0:
        buttonz.config(text = "O")
        flag = flag + 1

button1 = Button(root,command = ttt1)
button2 = Button(root,command = ttt2)
button3 = Button(root,command = ttt3)
buttona = Button(root,command = tttA)
buttonb = Button(root,command = tttB)
buttonc = Button(root,command = tttC)
buttonx = Button(root,command = tttX)
buttony = Button(root,command = tttY)
buttonz = Button(root,command = tttZ)


# def wincheck():
#     if 


        


button1.grid(row = 0, column = 0,padx = 10, pady = 10)
button2.grid(row = 0, column = 3,padx = 10, pady = 10)
button3.grid(row = 0, column = 6,padx = 10, pady = 10)
buttona.grid(row = 3, column = 0,padx = 10, pady = 10)
buttonb.grid(row = 3, column = 3,padx = 10, pady = 10)
buttonc.grid(row = 3, column = 6,padx = 10, pady = 10)
buttonx.grid(row = 6, column = 0,padx = 10, pady = 10)
buttony.grid(row = 6, column = 3,padx = 10, pady = 10)
buttonz.grid(row = 6, column = 6,padx = 10, pady = 10)

root.mainloop()