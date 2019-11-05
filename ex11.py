print("몇 살이죠?", end=' ')
age = input()
print("키는 몇이죠?", end=' ')
tall = input()
print("몸무게는 얼마죠?", end=' ')
weight = input()

explain = f"나이는 {age}살, 키는 {tall}, 몸무게는 {weight}이네요." 
print("네, " + explain)

name = input('잠깐만, 그렇다면 이름은 뭐죠? ')

print("{}씨, 당신의 {}".format(name, explain))