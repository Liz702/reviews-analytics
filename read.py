data = []
length = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		length += len(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('总共有', len(data), '笔留言')
print(data[0])#印出第一笔留言
print('--------')#视觉分隔 
print(data[1])#印出第二笔留言
length = float(length)
len1 = length / len(data)
print('留言平均长度为：', len1)