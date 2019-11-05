from sys import argv

filename, artist = argv

song = input(f"{artist}의 어떤 노래에 대한 정보를 알고 싶어요?: ")
print("{0}이란 곡의 정보는 아직 준비중입니다.".format(song))