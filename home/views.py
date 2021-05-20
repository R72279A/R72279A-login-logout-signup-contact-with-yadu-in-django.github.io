from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc)
        contact.save()
        messages.success(request, 'Your Message Has  been Sent!')

    return render(request, 'contact.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

#check for erroenus inputs
        if len(username) > 37:
            messages.error(request, "username must be under 37 carrectors")
            return redirect('/')

        if password1 != password2:
            messages.error(request, "Your Password Doesn't Match.")
            return redirect('/')
        

        my_user = User.objects.create_user(username, email, password1)
        my_user.save()
        messages.success(request, 'Your Account has been created!')

    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login Sucessful')
            return redirect('/')
        else:
            messages.error(request, 'No Such User, Please Try Again.')
            return redirect('/')

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.error(request, 'Logout Sucessful')
    return redirect('/')