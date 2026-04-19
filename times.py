
from tkinter import*
import numbers


root = Tk()
root.config(bg= "grey")
root.title("Multiplication")
lbl1= Label(root,text = "",width = 30)
lbl1.pack()
var = 1

def Times():
    global var
    s = ""
    for i in range(int(timeslimit.get())):
        ti = int(timestable.get())*var
        s = s + timestable.get() + "X" + str(var) + "=" + str(ti) + '\n'
        print(var,"=", ti)        
        var = var + 1
    lbl1.config (text = s )    
    


       


tt = ""
limit = ""

timestable = Entry(root,bg = "black", fg = "white",width= 20)
timestable.pack()

timeslimit = Entry(root, bg = "black", fg = "white", width = 20)
timeslimit.pack()

enter = Button(root,bg= "black",fg = "White", text = "Enter",command = Times )
enter.pack()



root.mainloop()

# s = ""

# for i in range(1, 11):
#   s  = s + '2' + 'X' + str(i) + '=' + str(2*int(i)) + '\n'
  
# print(s)