from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is the omaf app index view")


def register(request):
    return render(request, 'omaf_app/register.html')

def login(request):
    return HttpResponse("Login page")


def dashboard(request):
    return HttpResponse("Dashboard page")
