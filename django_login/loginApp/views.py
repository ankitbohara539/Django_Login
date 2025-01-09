from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout

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
            return render(request, 'loginApp/login.html', {'error': 'Invalid username or password'})
    return render (request,"loginApp/login.html",context)

def home(request):
    return render (request,"loginApp/home.html")

def index(request):
    return render (request, "loginApp/index.html")

def register(request):
    return render(request, "loginApp/register.html")


    