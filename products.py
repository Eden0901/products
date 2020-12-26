#检查档案在不在
import os #operating system 作业系统
products = []
if os.path.isfile('products.csv'):
	print('yeah! found it!')
	with open('products.csv', 'r') as f:
		for line in f:
			if '商品,价格' in line:
				continue #只能在回圈里写；功能就是跳到下一回
			name, price = line.strip().split(',') #line 是字串 可以用逗点来切割
			products.append([name, price])
	print(products)

else:
	print('file not found')
	
#让使用者输入
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price =	input('请输入商品价格:')
	price = int(price)
	p = []
	p.append(name)#建立二维度清单 清单里面再加上一个清单
	p.append(price)
	#或者写成 p = [name, price]
	products.append(p) #或者写成 products.append([name, price])
print(products)

products[0][0] #第一个‘0’指的是products清单中的第0格， 第二个‘0’指的是products 清单里的第0格的第0格

#印出所有购买记录
for p in products:
	print(p[0], '的价格是', p[1])
#'abc' + '123' = 'abc123'
#'abc' * 3 = 'abcabcabc'

#写入档案
with open ('products.csv', 'w', encoding='utf-8') as f: 
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #将四个字串合并成了一个字串



