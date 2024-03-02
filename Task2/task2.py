from tkinter import *
from decimal import *

root = Tk()
root.title('Calculator')

a = 15

buttons = [0] * a

activeStr = ''
stack = []

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))


def click(text):
    global activeStr
    global stack




for row in range(int(len(buttons))):
    for col in range(int(len(buttons))):
        button = Button(root, text=" ", width=2, height=1,
                command=lambda : click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()