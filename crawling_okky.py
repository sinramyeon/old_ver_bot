import requests
from bs4 import BeautifulSoup

def crawling_okky():
    url = 'https://okky.kr/articles/tech?query=&sort=id&order=desc'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'lxml')


    post_list = html.select('div > ul.list-group li.list-group-item div.list-title-wrapper h5 a')
    # print(post_list[0].get('href'))

    for post in post_list:
        print("{} - {}".format(post.get_text().strip(), "https://okky.kr" + post.get('href')))
        # print(post.get_text().strip(), end="\n")


if __name__ == "__main__":
    crawling_okky()
