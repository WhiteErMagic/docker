from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all()}
    object_list = Article.objects.all()
    # for assa in object_list:
    #     print(assa.scopes)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-published_at'

    return render(request, template, context)
