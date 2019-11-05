import sys
스크립트, 입력_인코딩, error = sys.argv

def main (언어_파일, 인코딩, errors):
    줄 = 언어_파일.readline()

    if 줄:
        줄_출력(줄, 인코딩, errors)
        return main(언어_파일, 인코딩, errors) # 재귀적으로 main 함수를 반복 호출한다.
    
def 줄_출력(줄, 인코딩, errors):
    다음_언어 = 줄.strip() # 문자열 양쪽에 있는 모든 한 칸 이상의 연속된 공백을 모두 지운다.
    생_바이트열 = 다음_언어.encode(인코딩, errors=errors) # 코드로 만든다
    요리한_문자열 = 생_바이트열.decode(인코딩, errors=errors) # 코드를 다시 문자열로 만든다.

    print(생_바이트열, "<===>",요리한_문자열)

언어들 = open("languages.txt", encoding='utf-8')

main(언어들, 입력_인코딩, error)