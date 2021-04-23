import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Arr = ['麻辣烫','麻辣拌','鸡公煲','渤海','打卤面','辣子鸡','羊汤'\
		,'二小','食堂','食堂','食堂','食堂'] # 给出列表
sum = np.array([0,0,0,0,0,0,0,0,0]) # 用于存储结果

# 实验部分
times=100000 # 实验次数
for i in range(times): # 循环次数
	conclu = Arr[random.randint(0, len(Arr)-1)] # 得出随机结果
	j = 0
	for t in Arr: # 将结果存入sum数组
		if(conclu == t):
			sum[j] += 1
			break
		else:
			j += 1

# 输出结果
print("麻辣烫 = {}\n麻辣拌 = {}\n鸡公煲 = {}\n渤海饭店 = {}\n打卤面 \
		= {}\n辣子鸡 = {}\n羊汤 = {}\\n二小饭店 = {}\n食堂(1/4) = {}\
		".format(sum[0],sum[1],sum[2],sum[3],sum[4],sum[5],sum[6],\
		sum[7],(sum[8])/4))

# Matplot统计图

# 设定显示字体
plt.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 横坐标内容
yy = ['麻辣烫','麻辣拌','鸡公煲','渤海饭店','打卤面','辣子鸡'\
		,'羊汤','二小饭店','食堂']

# 数据处理 将食堂值除以4以平衡结果
sum[8] = sum[8]/4

# 绘制结果统计柱状图
plt.bar(yy, sum)
plt.title('吃啥程序的合理性验证')
for x,y in enumerate(sum): # 绘制横坐标
	plt.text(x, y+100, '%s'%y, ha='center')
plt.show()

# 计算结果与理论概率的差值
pcs = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.])
for a in range(len(sum)):
	pcs[a] = sum[a]/times - 1/len(Arr)
print(pcs)

# 绘制差值柱状图
plt.bar(yy, pcs)
plt.title('差异值')
plt.show()
