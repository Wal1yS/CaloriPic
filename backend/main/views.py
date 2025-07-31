from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesFrom
from django.views.generic import DetailView, UpdateView, DeleteView

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'main/news_detail.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'main/create.html'
    form_class = ArticlesFrom
    context_object_name = 'article'

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'main/news_delete.html'
    context_object_name = 'article'
    success_url = '/news/' 


def index(request):
    return render(request, 'main/index.html')
def about(request):
    return render(request, 'main/about.html')
def news_home(request):
    articles = Articles.objects.order_by('-date')
    return render(request, 'main/news_home.html', {'articles': articles})
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Form is not valid'

    form = ArticlesFrom()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', data)