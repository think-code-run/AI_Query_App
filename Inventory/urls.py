from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.Homepage,name='home'),
    path('about/',views.AboutPage,name='about'),
    path('signup/',views.signupPage,name='signup'),
]