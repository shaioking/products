#檢查是否有檔案
import os #operating system

#讀取檔案
products = []
if os.path.isfile('products.csv'):#檢查檔案是否存在
	print('yeah!找到檔案了')
	with open('products.csv', 'r') as f:#encoding='utf-8'
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			#name = d[0]
			#price = d[1]
			products.append([name, price])
	print(products)
else:
	print('找不到檔案....')


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
	#products.append([name, price])
print(products)

#所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w') as f:#encoding='utf-8'
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')#txt 改成 csv