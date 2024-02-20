from . import views
from django.urls import path


urlpatterns = [
    path("login/", views.sing_in, name="login"),
]
