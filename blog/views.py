from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.


def blog(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'blog.html', {'articles': articles})


def article_full(request, slug):
    return HttpResponse(slug)
