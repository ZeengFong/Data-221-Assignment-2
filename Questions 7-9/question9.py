import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
content_div = soup.find('div', id='mw-content-text')

target_table = None
if content_div:
    tables = content_div.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        data_rows = [row for row in rows if row.find_all('td')]
        if len(data_rows) >= 3:
            target_table = table
            break

if target_table:
    all_rows = target_table.find_all('tr')
    header_tags = all_rows[0].find_all('th')
    
    extracted_data = []
    for row in all_rows:
        cols = row.find_all(['td', 'th'])
        extracted_data.append([c.get_text().strip() for c in cols])

    max_cols = max(len(r) for r in extracted_data)
    padded_data = [r + [''] * (max_cols - len(r)) for r in extracted_data]

    if header_tags:
        df = pd.DataFrame(padded_data[1:], columns=padded_data[0])
    else:
        df = pd.DataFrame(padded_data, columns=[f"col{i+1}" for i in range(max_cols)])

    df.to_csv('wiki_table.csv', index=False)