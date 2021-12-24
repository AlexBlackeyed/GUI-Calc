import tkinter as tk
from tkinter import ttk
from tkinter.constants import DISABLED, INSERT
from tkinter.font import NORMAL
from ttkthemes import ThemedStyle

root = tk.Tk()
style = ThemedStyle(root)
style.set_theme('yaru')
root.title("Calculator") 
root.geometry('340x480')
expression = []
def create_widgets():
    global result_box
    result_box = tk.Text(root,height=3,width=5,state=DISABLED)
    zero = ttk.Button(text=0,command=lambda index="0": universal_command(index))
    one = ttk.Button(text=1,command=lambda index="1": universal_command(index))
    two = ttk.Button(text=2,command=lambda index="2": universal_command(index))
    three = ttk.Button(text=3,command=lambda index="3": universal_command(index))
    four = ttk.Button(text=4,command=lambda index="4": universal_command(index))
    five = ttk.Button(text=5,command=lambda index="5": universal_command(index))
    six = ttk.Button(text=6,command=lambda index="6": universal_command(index))
    seven = ttk.Button(text=7,command=lambda index="7": universal_command(index))
    eight = ttk.Button(text=8,command=lambda index="8": universal_command(index))
    nine = ttk.Button(text=9,command=lambda index="9": universal_command(index))
    dot = ttk.Button(text='.',command=lambda index=".": universal_command(index))
    division = ttk.Button(text="/",command=lambda index="/": universal_command(index))
    multiplication = ttk.Button(text="*",command=lambda index="*": universal_command(index))
    plus = ttk.Button(text="+",command=lambda index="+": universal_command(index))
    minus = ttk.Button(text="-",command=lambda index="-": universal_command(index))
    equals = ttk.Button(text="=",command=equals_command)
    ce = ttk.Button(text="CE",command=clear_command)
    result_box.grid(row=0,column=0,columnspan=5,sticky=tk.W+tk.E)
    zero.grid(row=6,column=2,columnspan=2,sticky=tk.W+tk.E)
    one.grid(row=5,column=2)
    two.grid(row=5,column=3)
    three.grid(row=5,column=4)
    four.grid(row=4,column=2)
    five.grid(row=4,column=3)
    six.grid(row=4,column=4)
    seven.grid(row=3,column=2)
    eight.grid(row=3,column=3)
    nine.grid(row=3,column=4)
    dot.grid(row=6,column=4)
    division.grid(row=2,column=3)
    multiplication.grid(row=2,column=4)
    plus.grid(row=3,rowspan=2,column=5,sticky=tk.N+tk.S)
    minus.grid(row=2,column=5)
    equals.grid(row=5,rowspan=2,column=5,sticky=tk.N+tk.S)
    ce.grid(row=2,column=2)
    
def clear_command():
    result_box.configure(state=NORMAL)
    result_box.delete("1.0","end")
    expression.clear()
    result_box.configure(state=DISABLED)


def universal_command(i):
    result_box.configure(state=NORMAL)
    result_box.insert(INSERT,i)
    expression.append(i)
    result_box.configure(state=DISABLED)

def equals_command():
    final_str = "".join(expression)
    final_value = eval(final_str)
    result_box.configure(state=NORMAL)
    result_box.insert('2.0', '\n' + str(final_value))
    result_box.configure(state=DISABLED)


create_widgets()
root.mainloop()