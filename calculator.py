import tkinter as tk
import math


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

def sq():
    num1 = int(number1_entry.get())
    res = math.sqrt(num1)
    insert_values(res)

window = tk.Tk()
window.title('Калькулятор Алексея')
window.geometry('350x350')
window.resizable(False, False)
button_add = tk.Button(window, text='+', width=1, height=1, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text='-', width=1, height=1, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text='*', width=1, height=1, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text='/', width=1, height=1, command=div)
button_div.place(x=250, y=200)
button_square = tk.Button(window, text='Корень', width=5, height=1, command=sq)
button_square.place(x=40, y=200)
number1_entry = tk.Entry(window, width=27)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=27)
number2_entry.place(x=100, y=130)
answer_entry = tk.Entry(window, width=27)
answer_entry.place(x=100, y=280)
number1 = tk.Label(window, text='Введите первое число: ')
number1.place(x=100, y=50)
number2 = tk.Label(window, text='Введите второе число: ')
number2.place(x=100, y=105)
answer = tk.Label(window, text='Ответ: ')
answer.place(x=100, y=255)
window.mainloop()


