from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile
from .validators import validate_email


# Signup form with username, password and email
class SignUpForm(UserCreationForm):

    email = forms.EmailField(required=True, validators=[validate_email])

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Name'}),
            'password': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }
        fields = ('username', 'email', 'password1', 'password2',)


# Edit user's profile form
class EditProfileForm(UserChangeForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'first_name', 'last_name', 'gender', 'bio', 'tags', 'website', 'github', 'linkedin', 'facebook', 'status',)
