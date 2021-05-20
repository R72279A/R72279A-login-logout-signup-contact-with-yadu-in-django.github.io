from django.contrib import admin
from django.contrib.auth.models import User
from home.models import Contact
# from home.views import User

# Register your models here.
admin.site.register(Contact)

# admin.site.register(User)