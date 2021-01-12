data = []
count = 0
with open('original.txt', 'r') as f:
	for reviews in f:
		data.append(reviews)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
print('留言的平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(d), '筆資料小於100個字母')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料說good')
print(good[1])