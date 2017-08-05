import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# 인기시사 top 10 가져오기
def ddaily():
    count = 0;
    contents = {}
    # headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    html = requests.get('http://www.ddaily.co.kr/').text
    soup = BeautifulSoup(html,'html.parser')
    all_title=soup.select('.m01_arl266nn ul')
    for tag in all_title[0].select('li'):
        count+=1
        main_url="http://www.ddaily.co.kr"
        #제목이 짤림.. response 필요
        detail_url = urljoin(main_url,tag.find('a')['href'])
        html = requests.get(detail_url).text
        soup = BeautifulSoup(html,'html.parser')
        title_name=soup.select('.viewsubject .arvtitle .hbox h2')[0].text
        contents[title_name]=detail_url
        if(count==5):
            break;
    return contents