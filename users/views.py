from django.contrib.auth import authenticate, login
from django.shortcuts import render
from users.forms import LoginForm
from django.contrib import messages


# Create your views here.
def sing_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})
    elif request.metod == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi {username.title()} welcome back")

        messages.error(request, "Invalid username or password")
        return render(request, "users/login.html", {"form": form})
