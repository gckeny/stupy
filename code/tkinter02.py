# coding=gbk
import tkinter as tk

window = tk.Tk()
# ����һ�����ڶ���window
window.title('�ҵ��´���')
# ���ô������������
window.geometry('480x320')
# ���ô��ڵĴ�С
e = tk.Entry(window, show='*')
# ����һ������򣬲������������ݱ�����Ϊ*��,Ҳ���������������
e.pack()


def insert_point():
    var = e.get()
    t.insert('insert', var)


b1 = tk.Button(window, text='insert point', width=15, height=2, command=insert_point)
b1.pack()


def insert_end():
    var = e.get()
    t.insert(2.1, var)


# insert��һ������������Ϊ'insert'��������������ã���'end'������ǰ��������֮�󣬻�2.1����2�е�1��


b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()
t = tk.Text(window, height=2)
t.pack()
window.mainloop()
# ����ˢ�´��ڶ���������������
