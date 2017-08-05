import requests
from bs4 import BeautifulSoup
# 인기시사 top 10 가져오기 
def zdnet():
    count = 0;
    contents = {}
    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
    html = requests.get('http://www.zdnet.co.kr/news/news_list.asp?zdknum=0000&lo=z3',headers=headers).text
    soup = BeautifulSoup(html,'html.parser')
    for tag in soup.select('li div a'):
        count+=1
        title_name = tag.select('span')[0].text.strip()
        url = tag['href']
        contents[title_name]=url
        if(count==5):
            break;
    return contents

# print(zdnet())
