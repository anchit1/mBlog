from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSignupForm, UserLoginForm
from .models import User
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.

title_main = 'Micro Blog'


def index(request):
    context = { 'title_main': title_main, 'title_sub': 'Home'}
    return render(request, 'blog/index.html', context)


def signup(request):
    new_user = User()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        print ('username entered : ' + request.POST['username'])
        if form.is_valid():
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            p_hash = make_password(form.cleaned_data['password'])
            new_user.password_hash = p_hash
            new_user.save()

    else:
        form = UserSignupForm()
    context = {'title_main': title_main, 'title_sub': 'Sign Up', 'form': form, }
    return render(request, 'blog/signup.html', context)


def login(request):
    form = UserLoginForm()
    context = {'title_main': title_main, 'title_sub': 'Log In', 'form': form}
    return render(request, 'blog/login.html', context)


def about(request):
    return HttpResponse("This is the about page.")