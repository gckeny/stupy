# coding=gbk
import tkinter as tk

window = tk.Tk()
# 创建一个窗口对象window
window.title('我的新窗口')
# 设置窗口上面的名字
window.geometry('480x320')
# 设置窗口的大小
e = tk.Entry(window, show='*')
# 设置一个输入框，并设置输入内容被隐藏为*号,也可以设成其他符号
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()


def insert_end():
    var = e.get()
    t.insert(2.1, var)


# insert第一个参数可以设为'insert'，即光标所在外置，或'end'，即当前输入内容之后，或2.1即第2行第1列


b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()
window.mainloop()
# 不断刷新窗口对象，这样才能运行
