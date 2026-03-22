from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, WasteItemForm
from .models import WasteItem

def home(request):
    if request.user.is_authenticated:
        return redirect('submit')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

@login_required
def submit(request):
    if request.method == 'POST':
        form = WasteItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            messages.success(request, 'Item submitted successfully')
            return redirect('submit')
    else:
        form = WasteItemForm()
    items = WasteItem.objects.filter(user=request.user)
    return render(request, 'submit.html', {'form': form, 'items': items})

def user_logout(request):
    logout(request)
    return redirect('home')
