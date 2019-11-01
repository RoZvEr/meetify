
from django.contrib import admin
from django.urls import path, include, re_path
from index.views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static
from .settings import MEDIA_ROOT, MEDIA_URL
from accounts import views as acc

# All of website's urls
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('signup/', acc.signup),
    path('home/', acc.home, name='home'),
    path('logout/', acc.logout_view, name='logout'),
    path('login/', acc.login_view, name='login'),
    path('home/profile', acc.my_profile, name='my_profile'),
    path('home/profile/edit_profile', acc.edit_profile, name='edit_profile'),
    re_path(r'home/user/(?P<username>[a-zA-Z0-9]+)$', acc.view_profile, name='view_profile'),
    re_path(r'home_results/user/(?P<username>[a-zA-Z0-9]+)$', acc.view_profile, name='view_profile'),
    path('home/change_password', acc.change_password, name='change_password'),
    path('home_results/', acc.search, name='search'),
]

# Add static files and media url
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
