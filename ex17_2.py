from sys import argv
from os.path import exists

script, origin_file, copy_file = argv

if exists(copy_file):
    input_data = open(origin_file, encoding='utf-8').read() # 이런 식으로 파일을 열자마자 할 일을 할 일을 수행해서 다른 형으로 할당해버리면 굳이 파일을 닫을 필요가 없다.
    output_file = open(copy_file, 'w', encoding='utf-8').write(input_data)
    print(f"copy {len(input_data)}byte from {origin_file} to {copy_file}.")
else:
    print(f"there is no {copy_file}")
print("done.")