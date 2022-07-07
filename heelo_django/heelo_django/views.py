from django.http import HttpResponse
from django.shortcuts import render


def about(request):  #в функции передаем request запрос
    return render(request,'about.html')  #

def home (request):
    return HttpResponse('This is my home')