
import requests
response = requests.get("https://www.serebii.net/pokemon/gen1pokemon.shtml")

from bs4 import BeautifulSoup
# Finding the Table Class
soup = BeautifulSoup(response.content, 'lxml')
table1 = soup.find('table', class_='dextable')
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
headers.pop(3)
headers.pop(4)
headers.pop(1)
# Body Content
for i in table1.find_all('tr')[2:]:
    for j in i:
        content.append(j.text)
content = [i.removeprefix('\r\n\t\t') for i in content]
content = [i.removesuffix('\r\n\t\t') for i in content]
content = [i.replace('\n', '').replace(' ', '').replace('#', '') for i in content]
# for k in ignore:
#     content = [i.replace(k, '') for i in content]
content = [i for i in content if i]
# Finding Img Src
src = []
images = []
for i in table1.find_all('img'):
    src.append(i)
for element in src:
    if '.gif' not in element['src']:
        images.append("=IMAGE(\"" + "https://www.serebii.net"+element['src']+ "\")")

import pandas as pd
from datetime import datetime
data1 = pd.DataFrame(headers)
data2 = pd.DataFrame(content)
data2 = pd.DataFrame(data2[0].values.reshape(-1,9), columns=headers)
data2.insert(2, "Pic", images)
filename = datetime.now().strftime('gen1-%Y-%m-%d-%H-%M-%S.csv')
# data2.to_csv(filename, index=False)