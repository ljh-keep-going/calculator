from tkinter import *

def click(num):
    global op
    op = op + str(num)
    iptext.set(op)
# 点击数字 并保存在iptext里

def evaluate():
    global op
    output = str(eval(op))
    iptext.set(output)
# 求和 通过iptext里的式子进行运算

def clearDisplay():
    global op
    op = ""
    iptext.set(op)
# 清零，如果用remove，discard，pop就会比较繁琐，并且不确定它的数据，但可以通过全部读取的方式来清零，可以实现，内容繁琐

calc = Tk()
calc.title("Calculator")
op = ""
# 初始化数值
iptext = StringVar()
iparea = Entry(calc, bd=10, justify="right", textvariable=iptext).grid(columnspan=10)

bt7 = Button(calc, command=lambda: click(7), text="7", bd=5, padx=15,pady=10).grid(row=1, column=0)

bt8 = Button(calc,  command=lambda: click(8),  text="8", bd=5, padx=15,pady=10).grid(row=1, column=1)

bt9 = Button(calc,  command=lambda: click(9),  text="9", bd=5, padx=15,pady=10).grid(row=1, column=2)

add = Button(calc,  command=lambda: click('+'),  text="+", bd=5, padx=15,pady=10).grid(row=1, column=3)

bt4 = Button(calc,  command=lambda: click(4),  text="4", bd=5, padx=15,pady=10).grid(row=2, column=0)

bt5 = Button(calc,  command=lambda: click(5),text="5", bd=5, padx=15,pady=10).grid(row=2, column=1)

bt6 = Button(calc,  command=lambda: click(6), text="6", bd=5, padx=15,pady=10).grid(row=2, column=2)

sub = Button(calc,  command=lambda: click('-'), text="-", bd=5, padx=15,pady=10).grid(row=2, column=3)

bt1 = Button(calc,  command=lambda: click(1), text="1", bd=5, padx=15,pady=10).grid(row=3, column=0)

bt2 = Button(calc,  command=lambda: click(2),text="2", bd=5, padx=15,pady=10).grid(row=3, column=1)

bt3 = Button(calc, command=lambda: click(3),  text="3", bd=5, padx=15,pady=10).grid(row=3, column=2)

mul = Button(calc,  command=lambda: click('*'),text="*", bd=5, padx=15,pady=10).grid(row=3, column=3)

bt0 = Button(calc,  command=lambda: click(0), text="0", bd=5, padx=15,pady=10).grid(row=4, column=0)

btC = Button(calc,  command=clearDisplay,  text="C", bd=5, padx=15,pady=10).grid(row=4, column=1)

eql = Button(calc, command=evaluate,text="=", bd=5, padx=15, pady=10).grid(row=4, column=2)

div = Button(calc,  command=lambda: click('/'),  text="/", bd=5, padx=15,pady=10).grid(row=4, column=3)

calc.mainloop()






