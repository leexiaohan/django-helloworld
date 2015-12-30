#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    context = {}
    context['fruit'] = 'apple'
    return render(request, 'test.html', context)
def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'home.html', {'string': string})

def list(request):
    site1 = {'name': 'yangyu'}
    site2 = {'name': 'songci'}
    site3 = {'name': 'lixiaohan'}
    site_list = [site1, site2, site3]
    return render(request, 'home.html', {'site_list': site_list})
    #site_list = {'site1':site1, 'site2':site2, 'site3':site3}
    #site_list = ["HTML", "CSS", "jQuery", "Python", "Django"]

def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))