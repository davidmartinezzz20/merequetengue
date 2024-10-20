#Creating main file

import requests
from bs4 import BeautifulSoup

URL ="https://www.xataka.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="recent-posts")

with open('webpageContentFile', 'w' ,encoding='utf-8') as file: #Sending news to webpageContentFile
        try:
            file.write(results.prettify())
        except Exception as err:
            file.write('An ERROR occurred: '+ str(err)+ '\n')

titles = results.find_all("a", class_="head-new-item")

for title in titles:
    print(title.text, end="\n")
    href=title.get('href')
    href_url=URL+href
    print(href_url)
    
#Hasta aquí tenemos los títulos de las noticias y su respectivo href para poder abrirla