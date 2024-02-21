from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.


def signup_view(request):
    user_form=UserRegistrationForm()
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "sussessfully created an account.")
            return redirect('home')
    context={
        "forms":user_form
    }
    return render(request, "accounts/signup.html", context)

def logout_confirm(request):
    return render(request, "accounts/logout.html")