from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect

def demo(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def facultylogin(request):

    return render(request,'facultylogin.html')
def studentlogin(request):

    return render(request,'studentlogin.html',)

