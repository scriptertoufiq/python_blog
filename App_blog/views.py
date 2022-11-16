from django.shortcuts import render

# Create your views here.


def index(request):
    dic = {}
    return render(request, 'App_blog/blog_list.html',context=dic)
