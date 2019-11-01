from django.contrib import admin
from .models import Profile

# Add user profile to admin section
admin.site.register(Profile)
# Set admin site's name to Meetify
admin.site.site_header = 'Meetify'
