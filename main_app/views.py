from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *
from django.contrib.auth.decorators	import login_required

# Create your views here.

# Initial View
def splash(request):
    return render(request, 'splash.html')


def home(request):
    cities = City.objects.all()
    
    context = {'cities': cities}
    return render(request, 'home.html', context)


def city(request, city_name):
    city = City.objects.get(name=city_name)
    posts = city.post_set.order_by('-posted_date')
    post_form = Post_Form()
    print('POSTS HERE')
    print(posts)
    cities = City.objects.all()
    context = {"city": city, "posts": posts, "post_form": post_form, 'cities': cities}
    return render(request, 'cities/detail.html', context)


@login_required
def edit_profile(request, user_name):
    user = User.objects.get(username=user_name)
    profile = user.profile

    if request.method == 'POST':
        profile_edit_form = Profile_Edit_Form(request.POST, instance=profile)
        if profile_edit_form.is_valid():
            if request.user.username == user.username:
                profile = profile_edit_form.save()
                if 'image' in request.FILES:
                    profile.image = request.FILES['image']
                profile.save()

        return redirect ('profile', profile.user.username)
    profile_edit_form = Profile_Edit_Form(instance=profile)

    # cities = City.objects.all()
    context = {'profile_edit_form': profile_edit_form, 'profile': profile}
    return render(request, 'registration/edit.html', context)


def profile(request, user_name):
    user = User.objects.get(username=user_name)
    profile = user.profile
    cities = City.objects.all()

    # find which cities user has posted to
    posted_cities = []
    city_string = ""
    for post in profile.post_set.all():
        if post.city.name in posted_cities:
            pass
        else:
            city_string += post.city.name + ", "
            posted_cities.append(post.city.name)
    else:
        city_string = city_string[0:len(city_string)-2]

    context = {'profile': profile, 'cities': cities, 'city_string': city_string}
    return render(request, 'registration/profile.html', context)


def myprofile(request):
    user = request.user
    profile = user.profile
    cities = City.objects.all()
    posted_cities = []
    city_string = ""
    for post in profile.post_set.all():
        if post.city.name in posted_cities:
            pass
        else:
            city_string += post.city.name + ", "
            posted_cities.append(post.city.name)
    else:
        city_string = city_string[0:len(city_string)-2]

    context = {'profile': profile, 'cities': cities, 'city_string': city_string}
    return render(request, 'registration/profile.html', context)


@login_required
def create_post(request, city_name):
    city = City.objects.get(name=city_name)

    if request.method == "POST":


        post_form = Post_Form(request.POST, request.FILES)
        print(post_form.errors)

        if post_form.is_valid():

            new_post = post_form.save(commit=False)
            new_post.profile_id = request.user.id
            new_post.city_id = city.id
            

            if 'image' in request.FILES:
                new_post.image = request.FILES['image']

            new_post.save()
        return redirect('/cities/'+str(city.name))
    post_form = Post_Form()
    context = {"post_form": post_form, "city_id": city.id}
    return render(request, 'posts/create.html', context)
    
    
def post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comment_set.order_by('-posted_date')
    print('POST CITY IS')
    print(post.city)
    context = {'post': post, 'comments': comments}
    return render(request, 'posts/detail.html', context)



def about(request):
    user_form = User_Form()
    context = {'form': user_form}
    return render(request, 'about.html', context)


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        post_form = Post_Form(request.POST, request.FILES, instance=post)

        if post_form.is_valid():
            if request.user.id == post.profile.user_id:
                if 'image' in request.FILES:
                    post_form.image = request.FILES['image']

                post_form.save()

        return redirect('post', post_id)
    post_form = Post_Form(instance=post)
    context = {"post_form": post_form, "post_id": post_id}
    return render(request,'posts/edit.html', context)




@login_required
def delete_post(request, post_id, city_id):
    doomed_post = Post.objects.get(id=post_id)
    if request.user.id == doomed_post.profile.user_id:
        doomed_post.delete()
    else:
        return redirect('post', post_id)
    city = City.objects.get(id=city_id)
    return redirect('/cities/'+str(city.name))



def signup(request):
    # if post
    if request.method == "POST":
        # build out data from form
        username_form = request.POST['username']
        email_form = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # validate that passwords match
        if password == password2:
        # check if username exists in db
            if User.objects.filter(username=username_form).exists():
                context = {'error': 'Username is already taken.'}
                return render(request, 'splash.html', context)
            else:
                if User.objects.filter(email=email_form).exists():
                    context = {'error':'That email already exists.'}
                    return render(request, 'splash.html', context)
                else: 
                # if everything is ok create account
                    user = User.objects.create_user(
                        username=username_form, 
                        email=email_form, 
                        password=password)
                    user.save()
                    profile_form = Profile_Form()
                    new_profile = profile_form.save(commit = False)
                    new_profile.user_id = user.id
                    new_profile.name = user.username
                    new_profile.save()

                    login(request, user)

                    subject = 'Welcome Wayfarer'
                    message = 'You are registered! Feel free to add your travel experiences and tips to our community of travellers!'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email_form]
                    send_mail(subject, message, email_from, recipient_list)

                    return redirect('/myprofile/')
        else:
            context = {'error':'Passwords do not match'}
            return render(request, 'splash.html', context)
    else:
        # if not post send message, try again 
        context = {'error':'Your account was not created. Please try again.'}
        return redirect(request, '/myprofile/')

# COMMENTS controllers

@login_required
def create_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":

        comment_form = Comment_Form(request.POST)
        print(comment_form.errors)

        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.profile_id = request.user.id
            new_comment.post_id = post.id
            
            new_comment.save()
        return redirect('/posts/'+str(post.id))
    comment_form = Comment_Form()
    context = {"comment_form": comment_form, "post_id": post.id}
    return render(request, 'comments/create.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(id=comment.post_id)
    if request.method == "POST":
        comment_form = Comment_Form(request.POST, instance=comment)
        if comment_form.is_valid():
            if request.user.id == comment.profile.user_id:
                comment_form.save()
        return redirect('post', post.id)
    comment_form = Comment_Form(instance=comment)
    context = {"comment_form": comment_form, "comment_id": comment_id}
    return render(request,'comments/edit.html', context)


@login_required
def delete_comment(request, comment_id):
    doomed_comment = Comment.objects.get(id=comment_id)
    post = Post.objects.get(id=doomed_comment.post_id)
    if request.user.id == doomed_comment.profile.user_id:
        doomed_comment.delete()
    else:
        return redirect('post', post.id)
    return redirect('/posts/'+str(post.id))

