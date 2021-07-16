from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun(request):
    return render(request,"index.html")
def doctors(request):
    return render(request,"doctors.html")
def blog(request):
    return render(request,"blog.html")
def blogs(request):
    return render(request,"blog-single.html")
def opth(request):
    return render(request,"opthalmology.html")
def gyn(request):
    return render(request,"gynaecology.html")
def ent(request):
    return render(request,"ent.html")
def services(request):
    return render(request,"services.html")
