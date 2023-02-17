from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Article
from django.shortcuts import render


def index_view(request: WSGIRequest):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context=context)