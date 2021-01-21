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

with open('products.csv', 'w') as f:#encoding='utf-8'
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '元' + '\n')
#txt 改成 csv