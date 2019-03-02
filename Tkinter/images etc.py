import tkinter

window = tkinter.Tk()
window.title("Edureka")

#taking image from directory and storing the source in a variable

icon = tkinter.PhotoImage(file = r"C:\Users\Wannes\Downloads\ab14208c1b3870e0521278f6c25a4937.png")
label = tkinter.Label(window, image= icon)
label.pack()

window.mainloop()