from Hello.settings import AUTH_PASSWORD_VALIDATORS
from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=77)
    email = models.CharField(max_length=77)
    desc = models.TextField(max_length=777)
    def __str__(self):
            return self.name

# class User(forms.ModelForm):
#     username = models.CharField(max_length=77)
#     email = models.CharField(max_length=77)
#     password1 = models.CharField(max_length=77777)
#     password2 = forms.CharField(widget=forms.PasswordInput)