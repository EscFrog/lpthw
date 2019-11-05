def makeList(number, interval):
    숫자들 = []
    
    for i in range(0, number, interval):
        print(f"꼭대기에서 i는 {i}")
        숫자들.append(i)

        print("숫자는 이제: ", 숫자들)
        print(f"바닥에서 i는 {i}")
    
    '''
    i = 0
    while i < number:
        print(f"꼭대기에서 i는 {i}")
        숫자들.append(i)

        i = i + interval
        print("숫자는 이제: ", 숫자들)
        print(f"바닥에서 i는 {i}")
    '''

    print("리스트 안의 숫자: ")
    for 숫자 in 숫자들:
        print(숫자)

number = int(input("몇 이하의 숫자를 포함하고 싶어요?> "))
interval = int(input("간격은요?> "))

makeList(number, interval)