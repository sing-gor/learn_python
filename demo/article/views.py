
from django.shortcuts import render

# 从当前目录下 的models.py 导入 Article


def home(request):



    return render(request,template_name='home.html')


def article_list(request):

    return render(request, template_name='article_list.html')


def article_1(request):

    return render(request,  template_name='article_1.html')

def article_2(request):

    return render(request,  template_name='article_2.html')

def article_3(request):

    return render(request,  template_name='article_3.html')
    
def article_4(request):

    return render(request,  template_name='article_4.html')
