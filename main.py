#Creating main file

import requests
import os
from bs4 import BeautifulSoup

URL ="https://www.xataka.com"
page = requests.get(URL)
newsFile = "webPageNews"
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="recent-posts")

with open('webpageContentFile', 'w' ,encoding='utf-8') as file: #Sending news to webpageContentFile
        try:
            file.write(results.prettify())
        except Exception as err:
            file.write('An ERROR occurred: '+ str(err)+ '\n')

if os.path.exists(newsFile): 
    os.remove(newsFile)
    print(f"File '{newsFile}' deleted successfully.")
else: 
    print(f"File '{newsFile}' not found, hence creating.")

titles = results.find_all("a", class_="head-new-item")
dict = {}

for title in titles:
    new_title = title.text
    href=URL+title.get('href')
    dict[new_title.strip()] = href

import sendMail
sendMail