from urllib.request import urlopen
from bs4 import BeautifulSoup

def get_Naver_gsu():
    html = urlopen("https://www.naver.com/")    #html코드를 가져옴
    bsObj = BeautifulSoup(html, "html.parser")  #파싱(구문분석함)

    ingilist = bsObj.findAll("span", {"class":"ah_k"}, limit = 20)  #class="ah_k"인 span태그만 모음
    i = 0
    
    while(i < 20):      #20번 반복
        ingilist[i] = (ingilist[i]).get_text()      #태그를 떼고 태그의 내용만 가져옴
        i+=1

    return tuple(ingilist)  #튜플 반환

#인터프리터로 열 떄만 실행되는 코드들
i = 0
if __name__ == "__main__":
    ingilist = get_Naver_gsu()
    for gsu in ingilist:
        print("%d위. %s" %(i+1, gsu))
        i+=1