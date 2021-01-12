data = []
count = 0
with open ('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('計算完了，總共有', len(data), '筆資料')

#計算留言平均長度 平均長度=總長/總數  用for loop把資料拿出來後才能看長度
sum_length = 0
for d in data:
	sum_length += len(d)
print('留言平均長度是', sum_length/len(data), '個字')

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆留言自數小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good), 'reviews mentioned good.')