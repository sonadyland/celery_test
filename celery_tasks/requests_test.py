import requests
from bs4 import BeautifulSoup
from lxml import etree


url = 'https://www.runoob.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(response.text)
html = etree.HTML(response.text)
# print(html)
soup = BeautifulSoup(response.text, 'lxml')
print(type(html), type(soup), type(response), type(response.text),)
# print(soup)
name = html.xpath('/html/body/div[4]/div/div[2]/div[1]/a[1]/strong/text()')
# print(soup.prettify())
print(name)
# print(response.text)
