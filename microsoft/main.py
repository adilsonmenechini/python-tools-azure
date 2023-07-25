from bs4 import BeautifulSoup

import requests

html = requests.get("https://learn.microsoft.com/en-us/windows-server/get-started/kms-client-activation-keys").content

soup = BeautifulSoup(html, 'html.parser')

s = soup.find('div', class_='content')


title_element = s.find_all('tbody')


for title_element in title_element:
    title_elements = title_element.find('tr') 
    server = (title_elements)
    print(server.text.strip())
    print()
