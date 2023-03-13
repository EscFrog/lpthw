class 노래(object):

     # 초기화 할 때 가사 인수에 인자를 받는다. 밑에서 for 구문을 사용해야 하므로 iterable 형태로 받아야 한다.
    def __init__(self, 가사):
        self.가사 = 가사
    
    # 함수를 실행할 때, 현재 클래스로 생성된 수많은 객체 중 호출된 자기 자신임을 명시적으로 알려줘야 한다.
    def 노래_불러(self): 
        for 한줄 in self.가사:
            print(한줄)

# 객체 인스턴스화
obj1_celebrating = 노래(["생일 축하 합니다", "고소당하기는 싫으니까", "여기서 이만 할게요"])
obj2_bulls_on_parade = 노래(["조개 껍질 한가득 차고", "가장을 위한다지"])
obj3 = 노래("가나다라마바사") # string도 iterable이니까....
some_list = [""]

# 각 객체의 함수 호출
obj1_celebrating.노래_불러()
obj2_bulls_on_parade.노래_불러()
obj3.노래_불러()
