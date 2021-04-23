import random
import numpy as np
import tkinter as tk
import tkinter.messagebox
import time

# 给出可选内容，手动权重
Arr = ['麻辣烫', '麻辣拌', '鸡公煲', '渤海', '打卤面', '辣子鸡', '羊汤',
       '二小', '食堂', '食堂', '食堂', '食堂']
# 将结果保存到eat.txt
f = "eat.txt" 

# 按钮事件函数
def b1():
    text = Arr[random.randint(0, len(Arr)-1)]  # 得出随机结果
    with open(f, "a") as file:
        file.write(str(time.asctime(time.localtime(time.time()
                    ))) + " " + text + "\n")  # 写入txt格式
    tk.messagebox.showinfo('今晚吃：', text)  # 弹窗显示结果

# 定义窗口
win = tk.Tk()  
win.geometry('300x100')  # 窗口大小

# 窗口内容
l = tk.Label(win, text='点击下方按钮决定今晚吃啥', font=('Arial',
                                    12), width=30, height=2)
l.pack()
B = tk.Button(win, text="我是按钮", relief='raised', width=8,
              command=b1)
B.pack()

win.mainloop()
