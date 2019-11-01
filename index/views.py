from django.shortcuts import render
from accounts.views import home
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    user = request.user
    if bool(user.is_authenticated):
        return HttpResponseRedirect('home')
    else:
        return render(request, 'index.html')
