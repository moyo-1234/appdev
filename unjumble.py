import tkinter
from tkinter import*
import random

Wind = Tk()
word = {"ahev":"have","kacra":"crack","otsp":"stop","ghih":"high","bolge":"globe"}

lbl = Label(Wind,text = "Guess what the word is")
lbl.pack()

rword = random.choice(word)

jumb = Label(Wind,text = rword)
jumb.pack()



wtw = Entry(Wind,width = 30)
wtw.pack()















Wind.mainloop()