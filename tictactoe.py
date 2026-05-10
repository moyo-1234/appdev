import tkinter
from tkinter import*
import time
flag = 1
b1 = 0
b2 = 0
b3 = 0
ba = 0
bb = 0
bc = 0
bx = 0
by = 0
bz = 0
root = tkinter.Tk("900x900")

def wincheck1():
    if b1 == 1 and b2 == 1 and b3 == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif ba == 1 and bb == 1 and bc == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif bx == 1 and by == 1 and bz == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif b1 == 1 and ba == 1 and bx == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif b2 == 1 and bb == 1 and by == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif b3 == 1 and bc == 1 and bz == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif b1 == 1 and bb == 1 and bz == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    elif b3 == 1 and bb == 1 and bx == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")



def wincheck2():
    if b1 == 2 and b2 == 2 and b3 == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif ba == 2 and bb == 2 and bc == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif bx == 2 and by == 2 and bz == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b1 == 2 and ba == 2 and bx == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b2 == 2 and bb == 2 and by == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b3 == 2 and bc == 2 and bz == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b1 == 2 and bb == 2 and bz == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b3 == 2 and bb == 2 and bx == 2:
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
        



def ttt1():
    global flag
    global b1
    if flag == 1:
        button1.config(text = "X")
        flag = flag - 1
        b1 = b1 + 1
        wincheck1()
    elif flag == 0:
        button1.config(text = "O")
        flag = flag + 1
        b1 = b1 + 2
        wincheck2()

def ttt2():
    global flag
    global b2
    if flag == 1:
        button2.config(text = "X")
        flag = flag - 1
        b2 = b2 + 1
        wincheck1()
    elif flag == 0:
        button2.config(text = "O")
        flag = flag + 1
        b2 = b2 + 2
        wincheck2()

def ttt3():
    global flag
    global b3
    if flag == 1:
        button3.config(text = "X")
        flag = flag - 1
        b3 = b3 + 1
        wincheck1()
    elif flag == 0:
        button3.config(text = "O")
        flag = flag + 1
        b3 = b3 + 2
        wincheck2()

def tttA():
    global flag
    global ba
    if flag == 1:
        buttona.config(text = "X")
        flag = flag - 1
        ba = ba + 1
        wincheck1()
    elif flag == 0:
        buttona.config(text = "O")
        flag = flag + 1
        ba = ba + 1
        wincheck2()

def tttB():
    global flag
    global bb
    if flag == 1:
        buttonb.config(text = "X")
        flag = flag - 1
        bb = bb + 1
        wincheck1()
    elif flag == 0:
        buttonb.config(text = "O")
        flag = flag + 1
        bb = bb + 2
        wincheck2()

def tttC():
    global flag
    global bc
    if flag == 1:
        buttonc.config(text = "X")
        flag = flag - 1
        bc = bc + 1
        wincheck1()
    elif flag == 0:
        buttonc.config(text = "O")
        flag = flag + 1
        bc = bc + 2
        wincheck2()

def tttX():
    global flag
    global bx
    if flag == 1:
        buttonx.config(text = "X")
        flag = flag - 1
        bx = bx + 1
        wincheck1()
    elif flag == 0:
        buttonx.config(text = "O")
        flag = flag + 1
        bx = bx + 2
        wincheck2()


def tttY():
    global flag
    global by
    if flag == 1:
        buttony.config(text = "X")
        flag = flag - 1
        by = by + 1
        wincheck1()
    elif flag == 0:
        buttony.config(text = "O")
        flag = flag + 1
        by = by + 2
        wincheck2()


def tttZ():
    global flag
    global bz
    if flag == 1:
        buttonz.config(text = "X")
        flag = flag - 1
        bz = bz + 1
        wincheck1()
    elif flag == 0:
        buttonz.config(text = "O")
        flag = flag + 1
        bz = bz + 2
        wincheck2()

button1 = Button(root,command = ttt1)
button2 = Button(root,command = ttt2)
button3 = Button(root,command = ttt3)
buttona = Button(root,command = tttA)
buttonb = Button(root,command = tttB)
buttonc = Button(root,command = tttC)
buttonx = Button(root,command = tttX)
buttony = Button(root,command = tttY)
buttonz = Button(root,command = tttZ)
Winlbl = Label(root,text = "",fg = "gold")





        


button1.grid(row = 0, column = 0,padx = 10, pady = 10)
button2.grid(row = 0, column = 3,padx = 10, pady = 10)
button3.grid(row = 0, column = 6,padx = 10, pady = 10)
buttona.grid(row = 3, column = 0,padx = 10, pady = 10)
buttonb.grid(row = 3, column = 3,padx = 10, pady = 10)
buttonc.grid(row = 3, column = 6,padx = 10, pady = 10)
buttonx.grid(row = 6, column = 0,padx = 10, pady = 10)
buttony.grid(row = 6, column = 3,padx = 10, pady = 10)
buttonz.grid(row = 6, column = 6,padx = 10, pady = 10)
Winlbl.place(x = 50, y = 50)

root.mainloop()