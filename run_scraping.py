import codecs
import os
import sys


project = os.path.dirname(os.path.abspath('django_app/manage.py'))
sys.path.append(project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_app.settings'

import django
from django.db import DatabaseError

django.setup()

from scraping.models import Vacancy, City, Language, Error
from scraping.parsers import headhunter

parsers = (
    (headhunter, 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&fromSearch=true&text=Python&from=suggest_post'),
)



city = City.objects.filter(slug='moskva').first()
language = Language.objects.filter(slug='python').first()

works, errors = [], []
for func, url in parsers:
    w, e = func(url)
    works += w
    errors += e

for work in works:
    v = Vacancy(**work, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass
if errors:
    er = Error(data=errors).save()

# h = codecs.open('headhunter.txt', 'w', 'utf-8')
# h.write(str(works))
# h.close()
