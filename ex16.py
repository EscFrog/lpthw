from sys import argv

스크립트, 파일_이름 = argv

print(f"{파일_이름} 파일을 지우려 합니다.")
목적지 = open(파일_이름, encoding='utf-8') # 읽기 모드로 파일을 연다. 아무 옵션을 안 넣으면 읽기 모드로 열린다.
print("현재 파일 내용은 다음과 같습니다.")
print(목적지.read())
print("취소하려면 CTRL-C (^C) 를 누르세요.")
print("진행하려면 리턴 키를 누르세요.")
input("?")

print("파일 내용을 지웁니다. 안녕히!")
목적지 = open(파일_이름, 'w', encoding='utf-8') # 쓰기 모드로 파일을 다시 연다.
목적지.truncate()

print("이제 세 줄에 들어갈 내용을 부탁드릴게요.")

줄1 = input("1줄: ")
줄2 = input("2줄: ")
줄3 = input("3줄: ")

print("이 내용을 파일에 씁니다.")
목적지.write(f"{줄1}\n{줄2}\n{줄3}\n")

print(f"{파일_이름}의 새로운 내용은 다음과 같습니다.")
목적지 = open(파일_이름, 'r', encoding='utf-8') # 읽기 모드로 파일을 다시 연다.
print(목적지.read())
print("마지막으로 파일을 닫습니다.")
목적지.close() # 파일을 닫는다. 꼭 닫아줘야 함.