from django.shortcuts import render, redirect
from main.models import Articles
from main.forms import ArticlesForm

def news(request):
    return render(request, 'news/news_page.html')

def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incl')
        else:
            error = 'форма не добалена из-за ошибки'

    form = ArticlesForm()
    
    data = {
        "form": form,
        "error": error
        }
    
    return render(request, 'news/create.html', data)
