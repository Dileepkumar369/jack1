from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("hi amigos")
def rend_demo(request):
    return render(request,"sam.html")