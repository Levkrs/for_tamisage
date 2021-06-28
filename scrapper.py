import requests
from bs4 import BeautifulSoup

url = "https://russia24.pro/news/"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, 'html.parser')

all_news = []

class NewsElement():
    def __init__(self, title=None, timestamp=None, text=None, link=None, newsid=None):
        self.title = title
        self.timestamp = timestamp
        self.text = text
        self.link = link
        self.newsid = newsid

def get_news_text(url):
    url = url
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.find('div', class_='r24_text').text
    print('---')
    return text


def get_News_List():
    return soup.find('div', class_='r24NewsList')


x = get_News_List()


def filter_News(x):
    articles = x.find_all('div', class_='r24_article')
    arr_news = []
    for items in articles:
        news = NewsElement()
        info = items.find('div', class_='r24_info')
        news.newsid = info.parent.attrs['data-newsid']
        body = items.find('div', class_='r24_body')
        title = body.find('h3')
        title_text = title.find('span')
        news.timestamp = info.find('time').attrs['datetime']
        link = body.find('a')
        news.link = link.get('href')
        text = get_news_text(link.get('href'))
        news.text = text
        news.title = title_text.text
        arr_news.append(news)
        all_news.append(news)
    return arr_news


y = filter_News(x)
last_uid = int(y[-1].newsid)
for i in range(2):
    url = f"https://russia24.pro/news/_ajax/showmore/?from={last_uid}"
    response = requests.request("GET", url, headers=headers, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')

    resault = filter_News(soup)
    last_uid = int(resault[-1].newsid)


print('END')