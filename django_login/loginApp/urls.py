from .import views
from django.urls import path

urlpatterns = [
    path("",views.loginpage, name="login"),
    path("index/", views.index, name ="index"),
    path("home/", views.home, name ="home"),
    path("register/", views.register,name="register"),
    path("logout/", views.logout_page,name="logout"),
]  