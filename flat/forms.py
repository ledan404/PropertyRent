from django.contrib.auth.forms import UserCreationForm, forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput, TextInput


from flat.models import Profile


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User

        fields = ["username", "first_name", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class ProfileFormEdit(forms.ModelForm):

    class Meta:

        model = Profile

        fields = ["phone"]


class UserFormEdit(forms.ModelForm):

    class Meta:

        model = User

        fields = ["first_name", "email"]
