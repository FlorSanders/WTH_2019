import tkinter

window = tkinter.Tk()
window.title("Edureka")

#creating 3 diggerent functions for 3 different events

def left_click(event):
    tkinter.Label(window, text="Left Click!").pack()
    
def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()
    
def right_click(event):
    tkinter.Label(window, text="Right Click").pack()
    
window.bind("<Button-1>", left_click)
window.bind("<Button-2>",middle_click)
window.bind("<Button-3>", right_click)

window.mainloop()