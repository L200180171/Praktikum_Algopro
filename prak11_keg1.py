from Tkinter import Tk, Label, Entry, Button
from tkMessageBox import showinfo


my_app = Tk(className='coba-coba')

L1 = Label(my_app, text="DATA DIRI", font=("Times New Roman",20))
L1.grid(row=0, column=1)
L2 = Label(my_app, text="nama")
L2.grid(row=1, column=0)
E2 = Entry(my_app)
E2.grid(row=1, column=1)
L3 = Label(my_app, text="nim ")
L3.grid(row=2, column=0)
E3 = Entry(my_app)
E3.grid(row=2, column=1)
L4 = Label(my_app, text="buku favorit ")
L4.grid(row=3, column=0)
E4 = Entry(my_app)
E4.grid(row=3, column=1)
L5 = Label(my_app, text="idola ")
L5.grid(row=4, column=0)
E5 = Entry(my_app)
E5.grid(row=4, column=1)
L6 = Label(my_app, text="motto ")
L6.grid(row=5, column=0)
E6 = Entry(my_app)
E6.grid(row=5, column=1)
def quit():
    my_app.destroy()
B = Button(my_app, text="tutup",command=quit)
B.grid(row=6, column=1)
my_app.mainloop()
