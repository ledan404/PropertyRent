from django.http import HttpResponse

from django.shortcuts import redirect, render

from .models import Property, Address, Item

from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth

from django.contrib.auth import login, authenticate


# Create your views here.
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return HttpResponse("User was register")

    context = {"form": form}

    return render(request, "users/register.html", context=context)


def thelogin(request):

    form = LoginForm

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return HttpResponse("U log in!")

    context = {"form": form}

    return render(request, "users/login.html", context=context)


def logout(request):

    auth.logout(request)

    return redirect("/register")
