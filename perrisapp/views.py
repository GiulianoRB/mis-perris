from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def index(request):
    return render(request, 'perrisapp/index.html')

@login_required(login_url = "/accounts/login/")
def formulario(request):
    form = forms.AdoptarPerro()
    return render(request, 'perrisapp/formulario.html', {'form':form})