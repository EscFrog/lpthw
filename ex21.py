def plus(a,b):
    print(f"덧셈 {a} + {b}")
    return a + b

def minus(a, b):
    print(f"뺄셈 {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"곱셈 {a} * {b}")
    return a * b

def divide(a, b):
    print(f"나눗셈 {a} / {b}")
    return a / b

print("함수만으로 계산해봅시다!")

age = plus(30, 5)
tall = minus(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"나이: {age}, 키: {tall}, 몸무게: {weight}, IQ: {iq}")

print("문제를 하나 드릴게요.")
값 = plus(age, minus(tall, multiply(weight, divide(iq, 2))))
print("결과: ", 값, "손으로 계산할 수 있나요?")

print("400 / 20 * 12 + 2 - 3은?")
print(minus(plus(multiply(divide(400, 20), 12), 2), 3))

print("24 + 34 / 100 - 1023은?")
result = minus(plus(24, divide(34, 100)), 1023)
print(result)