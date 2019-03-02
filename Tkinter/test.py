import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as ms
win = tk.Tk()

win.title("WIDGETSSSS")

##defining geometry
win.geometry("350x200")

##labels
l1 = tk.Label(win, text="test", font=("Arial Bold", 10), fg="orange",bg="black")
l1.grid(column=1, row=0)


#buttons
bt = tk.Button(win, text="Enter")
bt.grid(column =4, row=0)

#functie gelinkt aan knop
def clicked():
    bt2.configure(text="button was clicked")
    print("goed")
bt2 = tk.Button(win, text="button2", command=clicked)
bt2.grid(column = 6,row =1)

##entry waarbij we iets invullen en dit wordt achter welcome to geplakt bij knopdruk
txt = tk.Entry(win, width=10)
txt.grid(column=1,row=6)
def geklikt():
    result = "Welcome to " + txt.get()
    l1.configure(text = result)
but = tk.Button(win,text="geklikt",command=geklikt)
but.grid(column=2,row=8)

##Combobox

combo = ttk.Combobox(win, values=["een","twee","drie"])

combo.grid(column = 0,row=10)

#checkbutton
chk_state = tk.BooleanVar()
chk_state.set(False)
chk = tk.Checkbutton(win, text="Select", var=chk_state)
chk.grid(column = 0, row = 15)

#radiobutton, 1 optie maximaak kiezen
rad1 = tk.Radiobutton(win, text="python", value = 1)
rad2 = tk.Radiobutton(win, text="Java", value = 2)
rad3 = tk.Radiobutton(win, text="C", value= 3)
rad1.grid(column=6,row=0)
rad2.grid(column=6,row=1)
rad3.grid(column=6,row=2)

#scrolledText
textTest = st.ScrolledText(win,width=40,height=10)
textTest.grid(column=4,row=0)
textTest.insert(tk.INSERT, "hier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je testier gaat je test")

##messagebox popt up bij klikken van knop
def opGeklikt():
    ms.showinfo("testTitel","inhoud van bericht")
btn = tk.Button(win,text="messageBox",command=opGeklikt)
btn.grid(column=0,row=0)

#spinbox

spint = tk.Spinbox(win, from_=0, to=30,width=5)
spint.grid(column=1,row=0)

#geometric management
#pack() neemt heel screen in
#grid()
#place() at specific position
win.mainloop()