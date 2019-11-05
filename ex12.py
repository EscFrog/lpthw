age = input("몇 살이죠? ")
tall = input("키는 몇이죠? ")
weight = input("몸무게는 얼마죠? ")

explain = f"나이는 {age}살, 키는 {tall}, 몸무게는 {weight}이네요." 
print("네, " + explain)

name = input('잠깐만, 그렇다면 이름은 뭐죠? ')

print("{}씨, 당신의 {}".format(name, explain))