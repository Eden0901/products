#检查档案在不在
import os #operating system 作业系统


def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue #只能在回圈里写；功能就是跳到下一回
			name, price = line.strip().split(',') #line 是字串 可以用逗点来切割
			products.append([name, price])
	return products

#让使用者输入
def user_input(products):
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
	return products

#products[0][0] 
#第一个‘0’指的是products清单中的第0格， 第二个‘0’指的是products 清单里的第0格的第0格

#印出所有购买记录
def print_products(products):
	for p in products:
		print(p[0], '的价格是', p[1])
	#'abc' + '123' = 'abc123'
	#'abc' * 3 = 'abcabcabc'

#写入档案
def write_file(filename, products):
	with open (filename, 'w', encoding='utf-8') as f: 
		f.write('商品,价格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n') #将四个字串合并成了一个字串

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yeah! found it!')
		products = read_file(filename)
	else:
		print('file not found')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

#重点：理想的function应该是做一件事， 所以refactor （重构程式）的核心概念， 就是把程式码不断的改写，写成
#越来越小的function，让function“尽量只做一件事
#程式最好有main（）function为程式的进入点
