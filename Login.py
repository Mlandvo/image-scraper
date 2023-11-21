from tkinter import *
import os
def command1(event):
    if entry1.get() == 'admin' and entry2.get() == 'password':
        root.destroy()
        os.system('python CompArch.py')

def command2():
    top.destroy()
    root.destroy()
    sys.exit()

root = Tk()
top = Toplevel()

top.geometry('300x260')
top.title('LOGIN SCREEN')
top.configure(background='white')
lbl1 = Label(top, text='Username:')
entry1 = Entry(top)
lbl2 = Label(top, text='Password:')
entry2 = Entry(top, show='*')
button2 = Button(top, text='Cancel', command=lambda:command2())

entry2.bind('<Return>', command1)

lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button2.pack()

root.withdraw()
root.mainloop()
