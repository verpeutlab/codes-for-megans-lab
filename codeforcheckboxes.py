from tkinter import *

#necessary for tkinter programs
root = Tk()
#not necessary simply labels the frame that pops up as DANNCE GUI (design element)
root.title('DANNCE GUI')

#defines all the variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()

#defines checkbuttons as c so they are easier to output using the grid function
c =Checkbutton(root, text="Left Ear", variable=var1)
c.grid(row=900, column=0)
c =Checkbutton(root, text="Right Ear", variable=var2)
c.grid(row=1800, column=0)
c =Checkbutton(root, text="Snout", variable=var3)
c.grid(row=2700, column=0)
c =Checkbutton(root, text="Spine F", variable=var4)
c.grid(row=3600, column=0)
c =Checkbutton(root, text="Spine M", variable=var5)
c.grid(row=4500, column=0)
c =Checkbutton(root, text="Tail Base", variable=var6)
c.grid(row=5400, column=0)
c =Checkbutton(root, text="Tail Mid", variable=var7)
c.grid(row=6300, column=0)
c =Checkbutton(root, text="Tail End", variable=var8)
c.grid(row=7200, column=0)
c =Checkbutton(root, text="Left Firepaw", variable=var9)
c.grid(row=8100, column=0)
c =Checkbutton(root, text="Left Wrist", variable=var10)
c.grid(row=9000, column=0)
c =Checkbutton(root, text="Left Elbow", variable=var11)
c.grid(row=9900, column=0)
c =Checkbutton(root, text="Left Shoulder", variable=var12)
c.grid(row=900, column=9000)
c =Checkbutton(root, text="Right Forepaw", variable=var13)
c.grid(row=1800, column=9000)
c =Checkbutton(root, text="Right Wrist", variable=var14)
c.grid(row=2700, column=9000)
c =Checkbutton(root, text="Right Elbow", variable=var15)
c.grid(row=3600, column=9000)
c =Checkbutton(root, text="Right Shoulder", variable=var16)
c.grid(row=4500, column=9000)
c =Checkbutton(root, text="Left Hindpaw", variable=var17)
c.grid(row=5400, column=9000)
c =Checkbutton(root, text="Left Ankle", variable=var18)
c.grid(row=6300, column=9000)
c =Checkbutton(root, text="Left Knee", variable=var19)
c.grid(row=7200, column=9000)
c =Checkbutton(root, text="Right Hindpaw", variable=var20)
c.grid(row=8100, column=9000)
c =Checkbutton(root, text="Right Ankle", variable=var21)
c.grid(row=9000, column=9000)
c =Checkbutton(root, text="Right Knee", variable=var22)
c.grid(row=9900, column=9000)
 
#necessary to close the tkinter program
root.mainloop()
