from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSignupForm

# Create your views here.

title_main = 'Micro Blog'

def index(request):
    context = { 'title_main': title_main, 'title_sub': 'Home'}
    return render(request, 'blog/index.html', context)


def signup(request):
    form = UserSignupForm()
    context = {'title_main': title_main, 'title_sub': 'Sign Up', 'form': form, }
    return render(request, 'blog/signup.html', context)


def login(request):
    return HttpResponse("This is the login page.")
