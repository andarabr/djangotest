from django.shortcuts import render
from .models import Article

def articles_list(request):
    article = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': article})
