#讀取檔案
products = []
with open('products.csv', 'r') as f:
	for line in f:
		if '商品, 價格' in line:
			continue
		name, price = line.strip().split(',')
		#name = d[0]
		#price = d[1]
		products.append([name, price])
print(products)

#請使用者輸入
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

#所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1], '元')

#寫入檔案
with open('products.csv', 'w') as f:#encoding='utf-8'
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '元' + '\n')
#txt 改成 csv