import tkinter as t

window=t.Tk()
window.title("label fills")

# creating 3 simple labels containing any text

#sufficient width
t.Label(window, text="suf width", fg="white", bg="purple").pack()

#width of x
t.Label(window, text="Taking all available x width", fg="white", bg="green").pack()

#height of y
t.Label(window, text = "Taking all available " ,fg="white", bg="black").pack(side = "left", fill = "y")