import yadisk

y = yadisk.YaDisk(token="your token here")
count = 0
count1 = 0
for i in list(y.listdir("your dir in yandex disk")):
	count += 1
print(f"всего файлов: {count}")


for i in list(y.listdir("your dir in yandex disk")):
	file_name = i['name']
	y.download(f'your dir in yandex disk/{file_name}', f'your dir for downloading{file_name}')
	count1 += 1
	print(f'успешно скачан {file_name}')
	print(f'всего скачано: {count1}')
