# Day  6
#Chapter 14: Status bar

from tkinter import *

def upload():
    statusvar.set("Please wait...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("started")

root = Tk()
root.geometry("420x200")

statusvar = StringVar()
statusvar.set("")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN)
sbar.pack(fill=X, side=BOTTOM, anchor="w")
Button(root,text="Update", command=upload).pack()

root.mainloop()


