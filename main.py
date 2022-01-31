import yadisk
from config import token as my_tkn
from config import source_dir
from config import dest_dir


y = yadisk.YaDisk(token=my_tkn)
count = 0
count1 = 0
for i in list(y.listdir(source_dir)):
	count += 1
print(f"всего файлов: {count}")


for i in list(y.listdir(source_dir)):
	file_name = i['name']
	y.download(f'{source_dir}{file_name}', f'{dest_dir}{file_name}')
	count1 += 1
	print(f'успешно скачан {file_name}')
	print(f'всего скачано: {count1}')
