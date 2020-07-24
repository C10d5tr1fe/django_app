import datetime
from django.shortcuts import render


def home(request):
    """Render Home page"""
    date = datetime.datetime.now().date()
    name = 'Dave'
    content = {'date': date, 'name': name}
    return render(request, 'base.html', content)
