from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.contrib.auth.models import User
from django.db.models import Q


# Main search for users
@login_required(login_url='/login')
def search(request):
    users = User.objects.all()
    query = request.GET.get("search_query")
    if query:
        users = users.filter(Q(username__icontains=query) |
                             Q(profile__tags__icontains=query) |
                             Q(profile__first_name__icontains=query) |
                             Q(profile__last_name__icontains=query) |
                             Q(profile__bio__icontains=query)
                             ).distinct()
    return render(request, 'home.html', {'users': users})


# Render the home page of the platform
@login_required(login_url='/login')
def home(request):
    users = User.objects.all()
    finalUsers = users[0:25]
    return render(request, 'home.html', {'users': finalUsers})


# Simple logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# Render current user's profile
@login_required(login_url='/login')
def my_profile(request):
    return render(request, 'profile.html', {'user': request.user})


# Edit current user's information
@login_required(login_url='/login')
def edit_profile(request):

    if request.method == 'POST':
        change_form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if change_form.is_valid():
            user = request.user
            user.profile.avatar = change_form.cleaned_data.get('avatar')
            user.profile.first_name = change_form.cleaned_data.get('first_name')
            user.profile.last_name = change_form.cleaned_data.get('last_name')
            user.profile.gender = change_form.cleaned_data.get('gender')
            user.profile.bio = change_form.cleaned_data.get('bio')
            user.profile.tags = change_form.cleaned_data.get('tags')
            user.profile.website = change_form.cleaned_data.get('website')
            user.profile.github = change_form.cleaned_data.get('github')
            user.profile.linkedin = change_form.cleaned_data.get('linkedin')
            user.profile.facebook = change_form.cleaned_data.get('facebook')
            user.profile.status = change_form.cleaned_data.get('status')
            user.first_name = user.profile.first_name
            user.last_name = user.profile.last_name
            user.save()
            change_form.save()
        return HttpResponseRedirect('/home/profile')



    else:
        change_form = EditProfileForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': change_form})


# Registration with username, password and email
def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            user.email = signup_form.cleaned_data.get('email')
            user.save()
            raw_password = signup_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(edit_profile)
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'form': signup_form})


# Login with username and password
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/home')
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form': login_form})


# View other user's profile
@login_required(login_url='/login')
def view_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'view_profile.html', {'user': user})


# Change user's password
@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST, user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            return HttpResponseRedirect('/home/profile')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': pass_form})
