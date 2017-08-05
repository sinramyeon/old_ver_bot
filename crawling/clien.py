import lxml.html
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def clien(w_recomenct,w_comment,limit_page=50):
    page = 0  #추천수  댓글수  읽어들일 페이지 파라메타 
    contents= {}
    while(True):
        list_url = "https://www.clien.net/service/board/news"
        main_url="https://www.clien.net"
        params = {
            'po':page,
        }  # 페이지 증가 
        page+=1
        if(page >limit_page): #일정 페이지 이상 검색 안함 
            return contents 
        html = requests.get(list_url,params=params).text
        soup = BeautifulSoup(html,'html.parser')
        try:
            soup.select('.card-grid .list-empty')[0].text
            return contents
        except:
            for tag in soup.select('.post-list .list-row'):
                try:
                    comment = int(tag.select('.badge-reply')[0].text)
                    good_number=tag.select('span')
                    recomend = int(good_number[0].text) #추천 수 
                    url = urljoin(main_url,tag.find('a')['href'])
                    title_url = tag.select('.list-title a')
                    title_name = title_url[0].text.strip() # 계시물 이름
                    if recomend >= w_recomenct and comment > w_comment: #추천 제한
                        choice = {
                            'url' : url,
                            # 'comment' : comment,
                            # 'recomend' : recomend,
                        }
                        contents[title_name]=choice
                except:
                    """  삭제된 계시물 """



# test=clien(1,10,1)  # 사용 예 
# print(test)