
import requests
from bs4 import BeautifulSoup
import pandas as pd

class PokeScraper():
    def __init__(self, url):
        self.url = url

    def get_header_info(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find('table', class_='dextable')
        headers = []
        for i in table.find_all('tr')[:2]:
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
        return headers

    def get_content_info(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find('table', class_='dextable')
        content = []
        for i in table.find_all('tr')[2:]:
            for j in i:
                content.append(j.text)
        content = [i.removeprefix('\r\n\t\t') for i in content]
        content = [i.removesuffix('\r\n\t\t') for i in content]
        content = [i.replace('\n', '').replace(' ', '').replace('#', '') for i in content]
        content = [i for i in content if i]
        return content

    def get_img_src(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'lxml')
        table = soup.find('table', class_='dextable')
        src = [i for i in table.find_all('img')]
        images = [("=IMAGE(\"" + "https://www.serebii.net"+element['src']+ "\")") for element in src if '.gif' not in element['src']]
        return images

    def create_df(self):
        poke_df = pd.DataFrame(self.get_content_info())
        poke_df = pd.DataFrame(poke_df[0].values.reshape(-1,9), columns=self.get_header_info())
        poke_df.insert(2, "Pic", self.get_img_src())
        poke_df.insert(loc = 0,column = 'Count',value = '')
        return poke_df