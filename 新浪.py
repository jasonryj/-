import requests
from bs4 import BeautifulSoup

url = 'https://finance.sina.com.cn/fund/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
news_items = soup.select('.news-item .list01 li a')
for item in news_items:
    title = item.get_text().strip()
    link = item['href']
    print(f"Title: {title}, Link: {link}")
