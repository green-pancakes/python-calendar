# Simple Calculator 
from tkinter import *

#   root window
root = Tk()
root.title('Simple Calculator')
menu = Menu(root)
root.maxsize(1000,1000)
root.configure(background='DarkSeaGreen3', menu=menu)
# a comment
def printSomething(x):
    def printer():
        Label(top_frame, text = str(x)).grid()
    return printer

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#   top frame stuff

top_frame = Frame(root, width=400, height=80, bg='DarkSeaGreen1')
top_frame.grid(row=0, column=1, columnspan=3, padx=15, pady=15)

#   create a bottom frame

bot_frame = Frame(root, width=400, height=600, bg='DarkSeaGreen1')
bot_frame.grid(row=1, column=0, columnspan=4, padx=15, pady=15)

#   create buttons for each number and operation in the bottom frame
#       top row
Button(bot_frame, text='7', command= printSomething(7), width=5).grid(row=1, column=1)
Button(bot_frame, text='8', command=lambda: print(8), width=5).grid(row=1, column=2)
Button(bot_frame, text='9', command=lambda: print(9), width=5).grid(row=1, column=3)
#       2nd row
Button(bot_frame, text='4', command=lambda: print(4), width=5).grid(row=2, column=1)
Button(bot_frame, text='5', command=lambda: print(5), width=5).grid(row=2, column=2)
Button(bot_frame, text='6', command=lambda: print(6), width=5).grid(row=2, column=3)
#       3rd row
Button(bot_frame, text='1', command=lambda: print(1), width=5).grid(row=3, column=1)
Button(bot_frame, text='2', command=lambda: print(2), width=5).grid(row=3, column=2)
Button(bot_frame, text='3', command=lambda: print(3), width=5).grid(row=3, column=3)
#       last row
Button(bot_frame, text='0', command=lambda: print(0), width=5).grid(row=4, column=1)
Button(bot_frame, text='.', command=lambda: print('.'), width=5).grid(row=4, column=2)
Button(bot_frame, text='+/-', command=lambda: print('+/-'), width=5).grid(row=4, column=3)

#   create a text window to display what's typed in the calculator

# Entry(top_frame, text="bbbb").grid(row=1, column=1)

# create a function to actually calculate what was typed(buttons) in the text box


root.mainloop()