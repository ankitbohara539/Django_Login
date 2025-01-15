from .import views
from django.urls import path

urlpatterns = [
    path("",views.loginpage, name="login"),
    path("index/", views.index, name ="index"),
    path("home/", views.home, name ="home"),
    path("register/", views.register,name="register"),
    path("logout/", views.logout_page,name="logout"),
    path("admindash/", views.admindash,name="admindash"),
    path('addlanguage/', views.add, name='add'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('view/', views.view_languages, name='view_languages')
]  