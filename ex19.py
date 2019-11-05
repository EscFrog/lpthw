def cheese_and_cracker(cheese_number, cracker_box):
    print(f"치즈가 {cheese_number}개 있어요!")
    print(f"크래커가 {cracker_box}상자 있어요!")
    print("파티 벌이기에 충분하네요!")
    print("담요 한 장 가져오세요.\n")

print("함수에 숫자를 바로 넣어줄 수 있습니다.")
cheese_and_cracker(20, 30)

print("스크립트의 변수를 쓸 수도 있구요.")
cheese_amount = 10
cracker_amount = 50
cheese_and_cracker(cheese_amount, cracker_amount)

print("안에서 계산을 해도 됩니다.")
cheese_and_cracker(10 + 20, 5 + 6)

print("합쳐서 변수도 쓰고 계산도 할 수도 있습니다.")
cheese_and_cracker(cheese_amount + 100, cracker_amount + 1000)