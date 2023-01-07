
import requests
response = requests.get("https://www.serebii.net/legendsarceus/pokemon.shtml")

from bs4 import BeautifulSoup
# Finding the Table Class
soup = BeautifulSoup(response.content, 'lxml')
table1 = soup.find('table', class_='tab')
headers = []
content = []
ignore = []
# Header Content
for i in table1.find_all('tr')[:2]:
    for j in i:
        headers.append(j.text)
headers = [i.removeprefix('\r\n\t\t') for i in headers]
headers = [i.removesuffix('\r\n\t\t') for i in headers]
headers = [i.removesuffix('\t') for i in headers]
headers = [i.replace('\n', '') for i in headers]
headers = [i for i in headers if i]
headers.pop(1)
headers.pop(2)
headers.pop(2)
# Body Content
for i in table1.find_all('tr')[2:]:
    for j in i:
        content.append(j.text)
content = [i.removeprefix('\r\n\t\t') for i in content]
# content = [i.removeprefix('\r\n\t\t') for i in content]
content = [i.removesuffix('\r\n\t\t') for i in content]
content = [i.replace('\n', '').replace(' ', '') for i in content]
# for k in ignore:
#     content = [i.replace(k, '') for i in content]
content = [i for i in content if i]

import pandas as pd
from datetime import datetime
data1 = pd.DataFrame(headers)
data2 = pd.DataFrame(content)
data2 = pd.DataFrame(data2[0].values.reshape(-1,8), columns=headers)
filename = datetime.now().strftime('arceus_data-%Y-%m-%d-%H-%M-%S.csv')
data2.to_csv(filename, index=False)
print(data2)