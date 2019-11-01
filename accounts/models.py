
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Model of basic user profile
class Profile(models.Model):
    status_choices = [
        (1, u'Ученик'),
        (2, u'Студент'),
        (3, u'Работещ'),
        (4, u'Любител'),
    ]
    gender_choices = [
        (1, u'Мъж'),
        (2, u'Жена'),
        (3, u'Не желая да посочвам'),
    ]
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    gender = models.IntegerField(choices=gender_choices, blank=False, default=1)
    tags = models.CharField(max_length=30000, blank=True)
    bio = models.TextField(max_length=300000, blank=True)
    website = models.CharField(max_length=500, blank=True)
    github = models.CharField(max_length=500, blank=True)
    linkedin = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    status = models.IntegerField(choices=status_choices, blank=False, default=1)

    def __str__(self):
        return str(self.user)


# Create user from the model
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Save user from the model
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
