
from django.shortcuts import render, get_object_or_404

# 从当前目录下 的models.py 导入 Article
from .models import Article


def home(request):
    context = {}
    '''
    Article.objects.all() 等同于下面的SQL语句

    SELECT
        id,
        title,
        body,
        author,
        created_time,
        update_time
    FROM articles;

    '''
    context['data'] = Article.objects.all()

    return render(request, context=context, template_name='home.html')


def article_list(request):
    context = {}
    context['data'] = Article.objects.all()
    return render(request, context=context, template_name='article_list.html')


def article_detail(request, pk):
    """
    SELECT
        id,
        title,
        body,
        author,
        created_time,
        update_time
    FROM articles
    WHERE id = <id>;

    """
    context = {}
    print(pk)
    context['data'] = get_object_or_404(Article, pk=int(pk))
    return render(request, context=context, template_name='article_detail.html')
