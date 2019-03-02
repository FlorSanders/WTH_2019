##grids

import tkinter

window = tkinter.Tk()
window.title("testGrid")

#2 input labels toevoegen

tkinter.Label(window, text="Username").grid(row=0) #this is placed in 00

##Entry is used to display the input field
tkinter.Entry(window).grid(row=0,column=1)
tkinter.Label(window, text="password").grid(row=1)#this is placed in 1 0
tkinter.Entry(window).grid(row = 1, column = 1)#this is placed in 1 1

#checkbutton is used to create te check buttons
tkinter.Checkbutton(window, text="Keep me Logged in").grid(columnspan=2)# columnspa tells width
window.mainloop()