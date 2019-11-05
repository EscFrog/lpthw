from sys import argv
from os.path import exists

script, origin_file, copy_file = argv

print(f"{origin_file} 에서 {copy_file} 로 복사합니다.")

input_file = open(origin_file, encoding='utf-8')
input_data = input_file.read()

print(f"입력 파일은 {len(input_data)}바이트입니다.")

print("출력 파일이 존재하나요? {}".format(exists(copy_file)))
print("준비되었습니다. 계속하려면 리턴을, 취소하려면 CTRL-C를 누르세요.")
input()

output_file = open(copy_file, 'w', encoding='utf-8')
output_file.write(input_data)

print("좋습니다. 모두 완료되었습니다.")

output_file.close()
input_file.close()