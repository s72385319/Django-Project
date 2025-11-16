from django.shortcuts import render, redirect
from main.models import Articles
from main.forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news(request):
    return render(request, 'news/news_page.html')


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/detail_view.html"
    context_object_name = "article"

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/create.html"
    # fields = ["title", "anons", "FULL", "date"]
    
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = "news/delete_view.html"
    success_url = "/incl/"


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
