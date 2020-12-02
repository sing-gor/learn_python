from django.shortcuts import render

def home(request):

    response = render(request,template_name='home.html')

    return response

def article_list(request):

    response = render(request, template_name='article_list.html')

    return response

def article_1(request):

    response = render(request,  template_name='article_1.html')

    return response

def article_2(request):

    response = render(request,  template_name='article_2.html')

    return response

def article_3(request):

    response = render(request,  template_name='article_3.html')

    return response

def article_4(request):

    response = render(request,  template_name='article_4.html')

    return response
