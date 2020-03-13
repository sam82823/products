products = []
while True:
	name = input('Enter the product name: ')
	if name == 'q': #quit
		break
	price = input('Enter the price: ')
	# p = [] #p as products
	# p.append(name) 
	# p.append(price) #p清單內放著name and price
    # p = [name, price] 這行等於第七到九行縮寫
	# products.append(p) #把p裝進products這個大清單
	products.append([name, price]) #直接把name跟price裝成小清單後裝到大清單products
print(products)

for p in products: # for loop 的寫法 執行表現方式不一樣 這個會一行行
	print(p[0], 'price is', p[1])