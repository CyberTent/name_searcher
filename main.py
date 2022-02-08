from bs4 import BeautifulSoup
import requests

id = [
# сюда id
]

f = open('data.txt','w')
for i in id:
    url=f'https://vk.com/id{i}'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html5lib") 
    f.write((str(soup.title).replace('<title>','').replace('</title>','').replace('|','').replace('ВКонтакте','')).rstrip()+',\n')
f.close()
