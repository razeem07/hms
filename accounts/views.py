from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from . import forms
from .forms import LoginForm

# Create your views here.
# class UserLoginView(LoginView):
#     template_name='accounts/login.html'
#     form_class=forms.LoginForm


def login_view(request):
    if request.method =='GET':
        return render(request,'accounts/login.html',{'form':forms.LoginForm()})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # change 'home' to your success page name
            return render(request, 'accounts/login.html', {'form': form})
           