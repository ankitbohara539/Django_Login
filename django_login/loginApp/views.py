from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ProgrammingLanguage
from .forms import ProgrammingLanguageForm


# Create your views here.


def loginpage(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('../home')
        else:
            return render(request, '/loginApp/login.html', {'error': 'Invalid username or password'})
    return render (request,"loginApp/login.html",context)

def home(request):
    return render (request,"loginApp/user/home.html")

def logout_page(request):
    logout(request)
    return redirect ('../')

def index(request):
    return render (request, "loginApp/index.html")

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
            user.save()
            messages.success(request, "Registration successful. Please login.")
            return redirect('../')
    return render(request, "loginApp/register.html")

# Admin dashboard displaying all programming languages

def admindash(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'loginApp/dashbord/admin.html', {'languages': languages})


def add(request):
    if request.method == 'POST':
        form = ProgrammingLanguageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admindash')  
    else:
        form = ProgrammingLanguageForm() 
    
    return render(request, 'loginApp/dashbord/form.html', {'form': form, 'action': 'Add'})


def update(request, pk):
    language = get_object_or_404(ProgrammingLanguage, pk=pk)
    if request.method == 'POST':
        form = ProgrammingLanguageForm(request.POST, request.FILES, instance=language)
        if form.is_valid():
            form.save()
            return redirect('admindash') 
    else:
        form = ProgrammingLanguageForm(instance=language) 
    
    return render(request, 'loginApp/dashbord/form.html', {'form': form, 'action': 'Edit'})

def delete(request, pk):
    language = get_object_or_404(ProgrammingLanguage, pk=pk)
    if request.method == 'POST':
        language.delete()  
        return redirect('admindash') 
    return render(request, 'loginApp/dashbord/delete.html', {'language': language})



def view_languages(request):
    languages = ProgrammingLanguage.objects.all()
    return render(request, 'loginApp/user/languages.html', {'languages': languages})
