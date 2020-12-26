products = []
while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price =	input('请输入商品价格:')
	p = []
	p.append(name)#建立二维度清单 清单里面再加上一个清单
	p.append(price)
	#或者写成 p = [name, price]
	products.append(p) #或者写成 products.append([name, price])
print(products)

products[0][0] #第一个‘0’指的是products清单中的第0格， 第二个‘0’指的是products 清单里的第0格的第0格

for p in products:
	print(p[0], '的价格是', p[1])