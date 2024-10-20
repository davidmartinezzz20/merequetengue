#Creating main file

import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.xataka.com")

soup = BeautifulSoup(response.content, "html.parser")

text = soup.get_text()

print(text)

with open('webpageContentFile', 'a+' ,encoding='utf-8') as file:
        try:
            file.write(text)
        except Exception as err:
            file.write('An ERROR occurred: '+ str(err)+ '\n')