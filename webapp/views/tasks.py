from django.shortcuts import render, redirect, reverse
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Article
from django.shortcuts import get_object_or_404


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'task_create.html')
    article_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'detailed_description': request.POST.get('detailed_description'),
        'date': request.POST.get('date'),
        'status': request.POST.get('status'),
    }
    article = Article.objects.create(**article_data)
    return redirect(reverse('article_detail', kwargs={'pk': article.pk}))


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'task.html', context=context)



