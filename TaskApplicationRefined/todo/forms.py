from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from todo.models import Task

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["task_name"]
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"})
        }