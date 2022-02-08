from bs4 import BeautifulSoup
import requests

file = 'id.txt' # файл с id страницами
ofile = open(file)

f = open('data.txt','w')
for i in ofile:
    id_page = i.replace(',','').rstrip()
    url=f'https://vk.com/id{id_page}'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html5lib") 
    print(str(soup.title).replace('<title>','').replace('</title>','').replace('|','').replace('ВКонтакте','').rstrip()+',')
    f.write((str(soup.title).replace('<title>','').replace('</title>','').replace('|','').replace('ВКонтакте','')).rstrip()+',\n')
f.close()
