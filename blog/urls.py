
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', blog),
    path('<slug:slug>', article_full)
]