# 选择困难症福音

你是不是也像我一样每天都会为决定晚上吃什么而感到困扰？为了不浪费每天饭点的宝贵时间给这个问题提供一个高效的解决方法，我编写了一个python程序来帮我们做选择。eat.py是主程序，eat.exe是它的可执行文件，其窗体由Tkinter生成；

![1](https://github.com/DesWudio/Dyschooia-Helper/blob/main/readme/img0.png)

可以通过修改eat.py中列表Arr的内容对程序可选项进行自定义，但是，这里我没有对选项权重进行设计，因此需要将权重高的选项在列表中手动多复制几次；

至于eat_reason.py的功能，出于信息类专业对数据的敏(bian)感(tai)和对计算机随机数随机性的怀疑，我的朋友们对它的公平性提出了质疑。于是，我在eat_reason.py中进行了1,000,000次实验并使用matplotlib生成了柱状图展示实验结果，对程序的公平性做出了证明。

![2](https://github.com/DesWudio/Dyschooia-Helper/blob/main/readme/img1.png)

# Dyschooia-Helper

Have difficulty in choosing what‘s for dinner? Don't hesitate too much, this python program is here to help you.

![3](https://github.com/DesWudio/Dyschooia-Helper/blob/main/readme/img0.png)

In eat.py, the optional range can be customized by modifying the contents of the list Arr. In addition, the form of eat.py is implemented by tkinter, make sure you have this lib.

![4](https://github.com/DesWudio/Dyschooia-Helper/blob/main/readme/img1.png)

Since my friends didn't trust the results of this program, eat_reason.py was used to prove the results fairness by conducting 1,000,000 experiments to test the probability distribution of each option. Finally, the results are displayed using matplotlib to plot bar graphs.
