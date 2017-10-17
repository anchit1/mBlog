from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

title_main = 'Micro Blog'

def index(request):
    context = { 'title_main': title_main, 'title_sub': 'Home'}
    return render(request, 'blog/index.html', context)


def signup(request):
    return HttpResponse("This is the signup page.")


def login(request):
    return HttpResponse("This is the login page.")
