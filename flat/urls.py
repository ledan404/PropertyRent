from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.thelogin, name="login"),
    path("logout/", views.logout, name="logout"),
    path("profile_edit/", views.profile_edit, name="profile_edit"),
    path("items/", views.items_page, name="items"),
    path("profile/", views.profile, name="profile"),
    path("profile/<username>/", views.profile_user, name="profile_user"),
]
