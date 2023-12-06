import requests
from bs4 import BeautifulSoup

url = 'https://xnews.jin10.com/53'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('p', class_='jin10-news-list-item-title')
for title in titles:
    print(title.get_text().strip())

url = 'https://xnews.jin10.com/53/page/2'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titles = soup.find_all('p', class_='jin10-news-list-item-title')
for title in titles:
    print(title.get_text().strip())