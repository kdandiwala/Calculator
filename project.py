from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background='white')
root.resizable(False, False)

console = StringVar()
console.set('')
window = Entry(root, textvariable = console)
text = str(window)
window.grid(row = 0, columnspan = 4, ipady=7)

def button_press(num): 
    global text 
    text = text + str(num) 
    console.set(text)

def clear_press(): 
    global text 
    text = "" 
    console.set("")


def equal_press(): 
    try: 
        global text 
        answer = str(eval(text))
        console.set(answer)
        
    except: 
        console.set("Error") 
        text = ""

#number button gui
one = Button(root, text = "1", fg = "black", bg = 'red', height=5, width=8, command=lambda: button_press(1))
two = Button(root, text = "2", fg = "black", height=5, width=8, command=lambda: button_press(2))
three = Button(root, text = "3", fg = "black", height=5, width=8, command=lambda: button_press(3))
four = Button(root, text = "4", fg = "black", height=5, width=8, command=lambda: button_press(4))
five = Button(root, text = "5", fg = "black", height=5, width=8, command=lambda: button_press(5))
six = Button(root, text = "6", fg = "black", height=5, width=8, command=lambda: button_press(6))
seven = Button(root, text = "7", fg = "black", height=5, width=8, command=lambda: button_press(7))
eight = Button(root, text = "8", fg = "black", height=5, width=8, command=lambda: button_press(8))
nine = Button(root, text = "9", fg = "black", height=5, width=8, command=lambda: button_press(9))
zero = Button(root, text = "0", fg = "black", height=5, width=16, command=lambda: button_press(0))

seven.grid(row=2, column=0)
eight.grid(row=2, column=1)
nine.grid(row=2, column=2)
four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)
one.grid(row=4, column=0)
two.grid(row=4, column=1)
three.grid(row=4, column=2)
zero.grid(columnspan=2, row=5, sticky = E)

#action button gui
decimal = Button(root, text = ".", fg = "black", height=5, width=8, command=lambda: button_press("."))
equal = Button(root, text = "=", fg = "black", height=5, width=8, command = equal_press)
clear = Button(root, text = "Clear", fg = "black", height=5, width=25, command = clear_press)
add = Button(root, text = "+", fg = "black", height=5, width=8, command=lambda: button_press("+"))
subtract = Button(root, text = "-", fg = "black", height=5, width=8, command=lambda: button_press("-"))
divide = Button(root, text = "/", fg = "black", height=5, width=8, command=lambda: button_press("/"))
multiply = Button(root, text = "x", fg = "black", height=5, width=8, command=lambda: button_press("*"))

decimal.grid(column = 2, row = 5)
equal.grid(column = 3, row = 5)
clear.grid(columnspan=3, row=1)
add.grid(row=1, column=3)
subtract.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)


root.mainloop()
