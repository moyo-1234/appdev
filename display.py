import tkinter

import tkinter

root = tkinter.Tk()
root.geometry("400x400")
root.config(bg="darkblue")
def Submit():
    lbl1.config(text=entr1.get())

lbl1 = tkinter.Label(root,text= "Please write your name underneath", fg= "gold", bg="black")
lbl1.pack()

entr1 = tkinter.Entry(root, width=30)
entr1.pack()

btn1 = tkinter.Button(root, text="Submit", bg = "black", fg="white", command=Submit)
btn1.pack()

root.mainloop()