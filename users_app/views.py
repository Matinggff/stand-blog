from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('pass')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_app:home')
            else:
                pass
    return render(request, "users_app/login.html", {})

def logout_user(request):
    logout(request)
    return redirect('home_app:home')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home_app:home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('pass1')
            password2 = request.POST.get('pass2')
            errors = []
            if User.objects.filter(username=username).exists():
                errors.append("Username already exists")

            if User.objects.filter(email=email).exists():
                errors.append("Email already exists")

            if password1 != password2:
                errors.append("Passwords do not match")

            if errors:
                return render(request, "users_app/register.html", {
                    "errors": errors,
                    "username": username,
                    "email": email,
                })

            User.objects.create_user(
                username=username,
                email=email,
                password=password1,
            )
            return redirect('users_app:login')
    return render(request, "users_app/register.html", {})
