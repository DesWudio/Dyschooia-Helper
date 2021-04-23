import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

Arr = ['麻辣烫','麻辣拌','鸡公煲','渤海','打卤面','辣子鸡','羊汤'\
		,'二小','食堂','食堂','食堂','食堂'] # 给出列表
sum = np.zeros(len(set(Arr))) # 用于存储结果

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

# Matplot统计图
# 设定显示字体
plt.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# 数据处理 将结果进行归一化
# 注意，这里要求Arr中所有选项都需要首先出现一次，否则在这里将无法索引
for i  in range(len(set(Arr))):
	sum[i] = sum[i]/(Arr.count(Arr[i]))

# 绘制结果统计柱状图
plt.bar(Arr[0:9], sum)
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
plt.bar(Arr[0:9], pcs)
plt.title('差异值')
plt.show()


# 输出结果
# for i  in range(len(set(Arr))):
	# print(str(Arr[i] + " = " + str(sum[i]/(Arr.count(Arr[i])))))


# print("麻辣烫 = {}\n麻辣拌 = {}\n鸡公煲 = {}\n渤海饭店 = {}\n打卤面 \
# 		= {}\n辣子鸡 = {}\n羊汤 = {}\\n二小饭店 = {}\n食堂(1/4) = {}\
# 		".format(sum[0],sum[1],sum[2],sum[3],sum[4],sum[5],sum[6],\
# 		sum[7],(sum[8])/4))
