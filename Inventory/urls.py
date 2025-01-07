from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Homepage,name='home'),
    path('about/',views.AboutPage,name='about'),
    path('signup/',views.signup,name='signup'),
    path('login/', views.loginPage, name='login'),
    path('upload/', views.uploadPage, name='upload'),
]