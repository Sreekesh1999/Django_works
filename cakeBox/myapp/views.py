from django.shortcuts import render,redirect
from django import forms
from django.views.generic import View
from myapp.models import Cakes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
class CakeForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields="__all__"
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "flavour":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "shape":forms.TextInput(attrs={"class":"form-control"}),
            "weight":forms.TextInput(attrs={"class":"form-control"}),
            "layer":forms.NumberInput(attrs={"class":"form-control"}),
            "descriptions":forms.Textarea(attrs={"class":"form-control","rows":3}),
            "photo":forms.FileInput(attrs={"class":"form-control"}),

        }

class RegistrationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class CakeBoxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm()
        return render(request,"cakebox-add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=CakeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Cake addedd successfully")
            return redirect("cakebox-list")
        messages.error(request,"Failed to add cake")
        return render(request,"cakebox-add.html",{"form":form})
    
class CakeBoxListView(View):
    def get(self,request,*args,**kwargs):
        qs=Cakes.objects.all().order_by("-date")
        return render(request,"cakebox-list.html",{"cakes":qs})
    
class CakeBoxDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Cakes.objects.get(id=id)
        return render(request,"cakebox-detail.html",{"cake":qs})
    
class CakeBoxDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Cakes.objects.get(id=id).delete()
        messages.success(request,"Removed cake successfully")
        return redirect("cakebox-list")
    
class CakeBoxEditview(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        form=CakeForm(instance=cake)
        return render(request,"cakebox-edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cake=Cakes.objects.get(id=id)
        form=CakeForm(data=request.POST,instance=cake,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated successfully")
            return redirect("cakebox-detail",pk=id)
        messages.error(request,"Invalid Update!!")
        return render(request,"cakebox-edit.html",{"form":form})
    
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect("signin")
        messages.error(request,"Failed to create the account!!")
        return render(request,"register.html",{"form":form})
    
class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            print(usr)
            if usr:
                login(request,usr) 
                messages.success(request,"Logged-In Successfully")
                return redirect("cakebox-add")
            messages.error(request,"Invalid login attempt!!")
            return render(request,"login.html",{"form":form})

    
    
    