from tkinter import *

window = Tk()
window.geometry("312x324") #size of window
window.resizable(0,0)# this prevents from resizing the window
window.title("Calculator")

#### functions

def btn_click(item):
    global expression
    expression = expression +str(item)
    input_text.set(expression)
    
#btn_clear function clears the input field
    
def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    result = str(eval)(expression) # eval evaluates the string expression directly
    input_text.set(result)
    expression =""
