"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addition/",views.AdditionView.as_view(),name="add"),
    path("subtraction/",views.SubtractionView.as_view(),name="sub"),
    path("multiplication/",views.MultiplicationView.as_view(),name="mul"),
    path("division/",views.DivisionView.as_view(),name="div"),
    path("cube/",views.CubeView.as_view(),name="cube"),
    path("factorial/",views.FactorialView.as_view(),name="fact"),
    path("primenumber/",views.PrimenumberView.as_view(),name="prime"),
    path("armstrong/",views.ArmstrongView.as_view(),name="armstrong"),
    path("palindrome/",views.PalindromeView.as_view(),name="palindrome"),
    path("evennumber/",views.EvennumbersView.as_view(),name="evennumber"),
    path("health/",views.HealthyView.as_view(),name="healthy"),
    path("temprature/",views.TempratureView.as_view(),name="temprature"),
    path("exponent/",views.ExponentView.as_view(),name="exponent"),
    path("login/",views.LoginView.as_view(),name="login"),
    path("registration/",views.RegistrationView.as_view(),name="registration"),
    path("geo/",views.GeoView.as_view(),name="geo"),
    path("",views.HomeView.as_view(),name="home"),
    

]
