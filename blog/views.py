from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserSignupForm, UserLoginForm, UserSignupForm2, NewPostForm
from .models import User, Post
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages, sessions
from django.contrib.messages import get_messages

# Create your views here.

title_main = 'Micro Blog'


def index(request):
    if request.session.get('remember_user') is not None:
        return redirect('feed', pk=request.session.get('remember_user'))
    if request.session.get('form_success') is not None:
        del request.session['form_success']

    context = {'title_main': title_main, 'title_sub': 'Home'}
    return render(request, 'blog/index.html', context)


def signup(request):
    new_user = User()
    err_list = []
    if request.method == 'POST' and request.session.get('form_success') is None:
        form = UserSignupForm(request.POST)
        if User.objects.filter(username=request.POST['username']).exists():
            err_list.append('username already exists.')
        if User.objects.filter(email=request.POST['email']).exists():
            err_list.append('An account with the entered email already exists.')
        if request.POST['password'] != request.POST['password_confirm']:
            err_list.append('The entered passwords do not match.')
        if len(request.POST['password']) < 6:
            err_list.append('The password is too short. (min. 6 characters')

        if form.is_valid() and len(err_list) == 0:
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            p_hash = make_password(form.cleaned_data['password'])
            new_user.password_hash = p_hash
            new_user.save()
            messages.add_message(request, messages.SUCCESS, 'Account created successfully. Log in to continue.')

            request.session['form_success'] = 'true'
            request.session['registered_user'] = new_user.username
            form2 = UserSignupForm2()
            context = {'title_main': title_main, 'title_sub': 'Sign Up', 'form': form2}
            return render(request, 'blog/signup2.html', context)

    elif request.method == 'POST' and request.session.get('form_success') == 'true':
        if request.session['registered_user'] is None:
            return HttpResponse('cookie not found.')
        else:
            user = User.objects.get(username=request.session['registered_user']);
            user.city = request.POST['city']
            user.country = request.POST['country']
            user.save()
            del request.session['registered_user']
            return redirect('login')

    else:
        form = UserSignupForm()
    context = {'title_main': title_main, 'title_sub': 'Sign Up', 'form': form, 'err_list': err_list}
    return render(request, 'blog/signup.html', context)


def login(request):
    form = UserLoginForm()
    msg = get_messages(request)
    err_list = []
    if request.method == 'POST' and User.objects.filter(username=request.POST['username']).exists():
        user = User.objects.get(username=request.POST['username'])
        if check_password(request.POST['password'], user.password_hash):
            request.session['current_user'] = user.username
            if request.POST.get('remember_me', 'off') == 'on':
                request.session['remember_user'] = user.username
            return redirect('feed', pk=user.username)

        else:
            err_list.append('Invalid username and/or password.')
    elif request.method == 'POST' and not User.objects.filter(username=request.POST['username']).exists():
        print('checkbox value: ' + request.POST.get('remember_me', 'off'))
        err_list.append('Invalid username and/or password.')

    else:
        form = UserLoginForm()

    context = {'title_main': title_main, 'title_sub': 'Log In', 'form': form, 'messages': msg, 'err_list': err_list}
    return render(request, 'blog/login.html', context)


def logout(request):
    if request.session.get('remember_user') is not None:
        del request.session['remember_user']
    request.session.flush()
    print(request.session.get('remember_user'))
    return redirect('home')


def about(request):
    return HttpResponse("This is the about page.")


def feed(request, pk):
    post_list= Post.objects.all();
    if request.method == 'POST':
        new_post = Post()
        new_post.content = request.POST['post_content']
        new_post.author = User.objects.get(username=request.session.get('current_user'))
        new_post.save()
        return redirect('feed', pk=request.session.get('current_user'))
        print(new_post.publish_date)
    return render(request, 'blog/feed_base.html', {'user': pk, 'post_list': post_list})


def test(request):
    return render(request, 'test/test_feed.html')
    # return HttpResponse('hello world')