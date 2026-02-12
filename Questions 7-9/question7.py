import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}


response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

if soup.title:
    print(f"title: {soup.title.string}")

content_div = soup.find('div', id='mw-content-text')
if content_div:
    paragraphs = content_div.find_all('p')
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) >= 50:
            print(f"\nFirst valid paragraph:\n{text}")
            break