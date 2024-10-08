from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
# logout
from django.contrib.auth import logout
# for profile decorators
from django.contrib.auth.decorators import login_required 
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Logout uchun
def custom_logout(request):
    logout(request)
    return redirect('login')

# Profile
@login_required
def profile(request):
    return render(request, 'users/profile.html')