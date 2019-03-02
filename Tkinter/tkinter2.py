import tkinter

window = tkinter.Tk()
window.title("TestWindow")

#creating 2 frames top and bottom
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")

#widgets in top and bottom frame
btn1 = tkinter.Button(top_frame, text = "Button1", fg="red").pack()
btn2= tkinter.Button(top_frame, text="Button2", fg="green").pack()
btn3 = tkinter.Button(bottom_frame,text="Button3", fg="purple").pack(side="left")
btn4 = tkinter.Button(bottom_frame,text="Button4", fg="orange").pack(side="left")

window.mainloop()