#                           Day 1 Starting of python Gui: Tkinter
from tkinter import *           # For gui


#chapter 1
root = Tk()         # a function used to make a empty window
#GUI code
#labels
label1 = Label(text = "This is the first line.")
label1.pack()

label2 = Label(text = "This is the second line.")
label2.pack()

label3 = Label(text = "This is the third line.")
# label3.pack()

#Geometry   also quize 1
root.geometry("733x434")     #if only used this can be resize to any size
root.minsize(200,150)        # resist to more minimize than this size
root.maxsize(1200,980)       # resist to more maximize than this size

label_wlcm_root = Label(text = "Ayodhya mein apka swagat hai")
label_wlcm_root.pack()

#display image using label



root = mainloop()     # a loop used to make a empty window
