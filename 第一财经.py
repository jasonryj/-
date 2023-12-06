import requests
from bs4 import BeautifulSoup

def fetch_yicai_news_titles(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    if response.status_code != 200:
        return "Error: Unable to fetch the webpage"

    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 直接查找所有h2标签
    titles = [h2.get_text().strip() for h2 in soup.find_all('h2')]

    return titles

# 指定URL
url = 'https://www.yicai.com/news/'

# 调用函数并打印标题
titles = fetch_yicai_news_titles(url)
for title in titles:
    print(title)
