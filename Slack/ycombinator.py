import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# 인기시사 top 10 가져오기
def ycombinator():
    count = 0;
    contents = {}
    html = requests.get('https://news.ycombinator.com/news').text
    url_main = 'https://news.ycombinator.com'
    soup = BeautifulSoup(html,'html.parser')
    all_title=soup.select('.m01_arl266nn ul')
    for tag in soup.select('.athing .title a'):
        count+=1
        url = tag['href'].strip()
        title = tag.text
        if not 'http' in url:
            url=urljoin(url_main,url)
        contents[title]=url
        if(count==5):
            break;
    return contents
