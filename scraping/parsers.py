"""Module for parcing informaton about works from sites: headhunter"""
import codecs
from random import randint
import requests
from bs4 import BeautifulSoup as BS


__all__ = ('headhunter')

HEADERS = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
     'Accept': '*/*', },
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.44',
     'Accept': '*/*', },
    {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 YaBrowser/20.7.1.70 Yowser/2.5 Safari/537.36',
     'Accept': '*/*', }
]
URL = 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&fromSearch=true&text=Python&from=suggest_post'


def headhunter(url):
    """Parcing headhunter"""
    resp = requests.get(url, headers=HEADERS[randint(0, 2)])
    works = []
    errors = []
    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find(
            'div', attrs={'data-qa': 'vacancy-serp__results'})
        if main_div:
            div_list = main_div.find_all(
                'div', attrs={'data-qa': 'vacancy-serp__vacancy'}
            )
            for div in div_list:
                title = div.find('span')
                href = title.a['href']
                details = div.find(
                    'div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'})
                requirements = div.find(
                    'div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'})
                employer = div.find(
                    'a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'})
                city = div.find(
                    'span', attrs={'data-qa': 'vacancy-serp__vacancy-address'})
                works.append({
                    'title': title.text,
                    'url': href,
                    'content': details.text,
                    'requirements': requirements.text,
                    'employer': employer.text,
                    'city': city.text
                })
        else:
            errors.append({
                'title': 'Div does not exists',
                'url': URL,
            })
    else:
        errors.append({
            'title': 'Page do not response',
            'url': URL,
        })
    return works, errors


if __name__ == '__main__':
    _works, _errors = headhunter(URL)
    h = codecs.open('headhunter.txt', 'w', 'utf-8')
    h.write(str(_works))
    h.close()
