
import requests
response = requests.get("https://www.serebii.net/blackwhite/pokemon.shtml")

from bs4 import BeautifulSoup
# Finding the Table Class
soup = BeautifulSoup(response.content, 'lxml')
table1 = soup.find('table', class_='tab')
headers = []
content = []
# Header Content
for i in table1.find_all('tr')[:2]:
    for j in i:
        headers.append(j.text)
headers = [i.removeprefix('\n\t\t') for i in headers]
headers = [i.removesuffix('\t\n\t\t') for i in headers]
headers = [i.removesuffix('\n\t\t') for i in headers]
headers = [i.replace('\n', '') for i in headers]
headers = [i for i in headers if i]
headers.pop(1)
headers.pop(2)
headers.pop(3)
# Body Content
for i in table1.find_all('tr')[2:]:
    for j in i:
        content.append(j.text)
content = [i.removeprefix('\n\n\t\t') for i in content]
content = [i.removeprefix('\n\t\t') for i in content]
content = [i.removesuffix('\n\t\t') for i in content]
content = [i.replace('\n', '').replace(' ', '').replace('Red-StripedForm', '').replace('Blue-StripedForm', '').replace('NormalZenMode', '').replace('ZenMode', '').replace('Normal', '').replace('AriaFormePirouetteForme', '').replace('AriaForme', '').replace('PirouetteForme', '') for i in content]
content = [i for i in content if i]

import pandas as pd
from datetime import datetime
data1 = pd.DataFrame(headers)
data2 = pd.DataFrame(content)
data2 = pd.DataFrame(data2[0].values.reshape(-1,9), columns=headers)
filename = datetime.now().strftime('bw_data-%Y-%m-%d-%H-%M-%S.csv')
data2.to_csv(filename, index=False)
print(data2)