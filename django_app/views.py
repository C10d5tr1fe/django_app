import datetime
from django.shortcuts import render


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    content = {'date': date, 'name': name}
    return render(request, 'base.html', content)
