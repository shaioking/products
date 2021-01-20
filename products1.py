products = []
while True:
	name = input('產品名稱: ')
	if name == 'q':
		break
	price = input('產品價格: ')
	p = []
	p.append(name)
	p.append(price)
	# = p = [name, price]
	products.append(p)
	# = products.append([name, price])
print(products)
for p in products:
	print(p[0], '的價格是', p[1], '元')