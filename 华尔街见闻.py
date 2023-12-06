import requests
from bs4 import BeautifulSoup

# 网址可能需要根据实际情况进行调整
url = 'https://wallstreetcn.com/news/hot'

# 发送请求获取网页内容
response = requests.get(url)
response.encoding = 'utf-8'  # 根据网站的编码调整

# 使用BeautifulSoup解析网页
soup = BeautifulSoup(response.text, 'html.parser')

# 寻找包含标题的特定div，根据提供的HTML结构进行定位
article_divs = soup.find_all('div', {'class': 'article-entry list-item'})

# 提取并打印所有标题
for article_div in article_divs:
    title_span = article_div.find('span', {'data-v-2b064c34': ''})
    if title_span:
        title = title_span.text.strip()
        print(title)
