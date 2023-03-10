from django.shortcuts import render
from .models import *

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request,
                  'article/list.html',
                  {'articles': articles})
