import os
import sys
import requests
from bs4 import BeautifulSoup

# https://okky.kr/articles/tech?offset=40&max=20&sort=id&order=desc

# recommend_url = "https://okky.kr/articles/tech?query=&sort=voteCount&order=desc"
recommend_url = "https://okky.kr/articles/tech?offset=0&max=5&sort=voteCount&order=desc"
# https://okky.kr/articles/tech?offset=20&max=20&sort=voteCount&order=desc

url = "https://okky.kr"


def get_blog_lists():
    response = requests.get(recommend_url)

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('h5.list-group-item-heading')

    title_dict = {}
    for link in links:
        # 링크 가져오기
        title_link = link.find('a')['href']
        title_link = url + str(title_link)
        # 타이틀 가져오기
        title = link.text.strip()

        title_dict.update({title: title_link})

    return title_dict
