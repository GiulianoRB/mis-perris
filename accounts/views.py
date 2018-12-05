from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #registra el usuario
            login(request, user)
            return redirect('perrisapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form':form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #loguear usuario
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('perrisapp:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form':form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('perrisapp:index')

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    profile = Profile.objects.create(user=user)
    profile.save()