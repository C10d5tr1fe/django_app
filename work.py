import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
           'Accept': '*/*',}
domain = 'https://hh.ru/'
url = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&fromSearch=true&text=Python&from=suggest_post'
resp = requests.get(url, headers=headers)
works = []
if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', attrs={'data-qa':'vacancy-serp__results'})
    div_list = main_div.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
    for div in div_list:
        title = div.find('span')
        href = title.a['href']
        works.append({'title':title.text, 'url': href})
    print(works) #проверка вывода данных на консоль


h = codecs.open('work.html', 'w', 'utf-8')
h.write(str(resp.text))
h.close()
