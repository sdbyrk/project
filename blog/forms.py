# Django
from django import forms
from django.contrib.auth import authenticate, get_user_model, login

# Local Django
from users.models import User


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")
        return super(LoginForm, self).clean(*args, **kwargs)
