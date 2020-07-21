from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    content = {'date': date, 'name': name}
    return render(request, 'base.html', content)
