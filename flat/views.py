from django.shortcuts import get_object_or_404, redirect, render
from django.template import context
from django.urls import resolve

from .models import Property, Address, Item, Profile

from .forms import CreateUserForm, LoginForm, UserFormEdit, ProfileFormEdit
from django.conf import settings


from django.contrib.auth.models import User, auth

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(user=user)

            return redirect("/login/")

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

                return redirect("/profile")

    context = {"form": form}

    return render(request, "users/login.html", context=context)


def logout(request):
    auth.logout(request)

    return redirect("/register")


def index(request):
    return render(request, "index.html")


def items_page(request):
    return render(request, "items_page.html")


@login_required
def profile(request):

    profile = Profile.objects.get(user=request.user)

    context = {"profile": profile}

    return render(request, "users/profile.html", context)


@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = UserFormEdit(instance=request.user, data=request.POST)

        profile_form = ProfileFormEdit(instance=request.user.profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()

            profile_form.save()

            return redirect("profile")

        else:
            context = {"user_form": user_form, "profile_form": profile_form}
            return render(request, "users/profile_edit.html", context=context)

    else:
        user_form = UserFormEdit(instance=request.user)
        profile_form = ProfileFormEdit(instance=request.user.profile)

        context = {"user_form": user_form, "profile_form": profile_form}

        return render(request, "users/profile_edit.html", context=context)


def profile_user(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    url = resolve(request.path).url_name

    context = {
        "profile": profile,
        "url": url,
        "user": user,
    }

    return render(request, "users/profile_user.html", context)
