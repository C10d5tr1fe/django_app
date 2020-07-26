import codecs
import os
import sys
import django
from django.conf import settings
from scraping.models import Vacancy, City, Language
from scraping.parsers import headhunter


project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)
# if not settings.configured:
#    settings.configure(**locals())
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_app.settings")
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_app.settings'
django.setup()


parsers = (
    (headhunter, 'https://hh.ru/search/vacancy?area=1&st=searchVacancy&fromSearch=true&text=Python&from=suggest_post'),
)

city = City.objects.filter(slug='moskva')
works, errors = [], []
for func, url in parsers:
    w, e = func(url)
    works += w
    errors += e

h = codecs.open('headhunter.txt', 'w', 'utf-8')
h.write(str(works))
h.close()
