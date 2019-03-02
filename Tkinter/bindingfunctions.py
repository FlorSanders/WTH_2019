import tkinter

window = tkinter.Tk()
window.title("GUI")

#creating a function called say_hi()
def say_hi(event):
    tkinter.Label(window, text = "Hi").pack()
    
btn = tkinter.Button(window,text = "Click Me!")
btn.bind("<Button-1>", say_hi)
btn.pack()
window.mainloop()