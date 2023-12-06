import requests
from bs4 import BeautifulSoup

url = 'https://cn.wsj.com/zh-hans/news/china'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('span', class_='WSJTheme--headlineText--He1ANr9C')
for title in titles:
    print(title.get_text().strip())
soup = BeautifulSoup(response.content, 'html.parser')
article_titles = soup.find_all('span', class_='WSJTheme--headlineText--He1ANr9C')
for title in article_titles:
    print(title.get_text().strip())
