# Django
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Local Django
from raven.forms import LoginForm
from users.models import User


class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form': form})


def IndexView(request):

    return render(request, 'index.html')
