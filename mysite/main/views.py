from django.shortcuts import render
from .models import Articles

def index(request):
    return render(request, 'main/index.html')

def incl(request):
    news = Articles.objects.all()
    return render(request, "main/incl.html", {"news": news})

def test(request):
    data = {
    'title': 'Тестовая страница',
    'item': ["about", "support", "FAQ"],
    'obj': {
        'text': "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source."
    }
}
    return render(request, 'main/test.html', data)