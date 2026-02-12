import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

content_div = soup.find('div', id='mw-content-text')
exclude = ["References", "External links", "See also", "Notes"]
valid_headings = []

if content_div:
    h2_tags = content_div.find_all('h2')
    for h2 in h2_tags:
        text = h2.get_text().replace('[edit]', '').strip()
        if text and not any(word in text for word in exclude):
            valid_headings.append(text)

with open('headings.txt', 'w') as f:
    for h in valid_headings:
        f.write(h + '\n')