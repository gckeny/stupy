# !/usr/bin/python
# -*- coding: UTF-8 -*-
from logging import root
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

def ui_process():
    root =Tk()
    root.geometry("300x400+300+200")

#标签
    L_titile = Label(root,text='藁 城 L T',)
    L_titile.config(font='Helvetica -18 bold',fg='blue')
    L_titile.place(x=150,y=20,anchor="center")
    L_author = Label(root, text='作者:Tjy')
    L_author.config(font='Helvetica -11 bold')
    L_author.place(x=230,y=380)


#按钮
    B_0 = Button(root, text="对话框", command=CreatDialog)
    B_0.place(x=90,y=200)
    B_1 = Button(root, text="确定", command=print)
    B_1.place(x=150, y=200)
    B_OK = Button(root,text="创建",command=lambda:button_process(root))
    B_OK.place(x=200,y=200)
    B_NO = Button(root, text="取消")
    B_NO.place(x=250,y=200)

#单选按钮
    v = IntVar()
    R_ONE=Radiobutton(root, text="One", variable=v, value=1,command=lambda:Print_b(1)).place(x=60,y=150)
    R_TWO=Radiobutton(root, text="Two", variable=v, value=2,command=lambda:Print_b(2)).place(x=10,y=150)

#滑块
    W = Scale(root, from_=0, to=100,orient=HORIZONTAL)#orient=HORIZONTAL 横向，默认纵向
    W.place(x=50,y=300)
    print(W.get())  #获取滑块值

#菜单栏
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_command(label="Save", command=SaveFile)
    # filemenu.add_separator()#分割线
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    mainloop()

#按钮对应函数入口
def button_process(root):
    #创建消息框
    messagebox.askokcancel('Python Tkinter', '确认创建窗口？')
    messagebox.askquestion('Python Tkinter', "确认创建窗口?")
    messagebox.askyesno('Python Tkinter', '是否创建窗口？')
    messagebox.showerror('Python Tkinter', '未知错误')
    messagebox.showinfo('Python Tkinter', 'hello world')
    messagebox.showwarning('Python Tkinter', '电脑即将爆炸，请迅速离开')
    root1 = Toplevel(root)

def PrintHello():
    print("hello")

def Print_b(a):
    print(a)

#创建对话框
def CreatDialog():
    #world = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue = 'Python Tkinter')
    window = Tk()
    # 创建一个窗口对象window
    window.title('配置窗口')
    # 设置窗口上面的名字
    window.geometry('480x160')
    # 设置窗口的大小
    l=Label(window,text="用户名:")
    l.grid(row=2,column=4)
    # 设置一个输入框，,也可以设成其他符号
    e = Entry(window)
    e.grid(row=2, column=5)
    l1=Label(window,text="密码:")
    l1.grid(row=2,column=6)
    e1 = Entry(window, show='*')
    # 设置一个输入框，并设置输入内容被隐藏为*号,也可以设成其他符号
    e1.grid(row=2, column=7)
    b =Button(window,text="完成",command=print(e.get(),e1.get()))
    b.grid(row=2,column=8)
    #print(world)
    # simpledialog.askinteger()
    # simpledialog.askfloat()

# 文件操作的对话框
def OpenFile():
    f = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(f)
    # 可使用os 模块运行文件


def SaveFile():
    f = filedialog.asksaveasfilename(title='保存文件', initialdir='d:\mywork', initialfile='hello.py')
    print(f)
    #可调用OS模块保存


if __name__ == "__main__":
    print("开始")
    ui_process()
#景
# 链接：https://www.jianshu.com/p/19d96f7107a0
# 來源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。