from django.shortcuts import render,redirect
from django.views.generic import View
from todo.forms import RegistrationForm,LoginForm,TaskForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from todo.models import Task


# Create your views here.
class SignUpView(View):
    model=User
    template_name="register.html"
    form_class=RegistrationForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})   

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            messages.success(request,"Account has been created")
            return redirect("signin")
        messages.error(request,"Failed to create account")
        return render(request,self.template_name,{"form":form})

class SignInView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Successfully loged-in")
                return redirect("index")
            messages.error(request,"Invalid credentials")
            return render(request,self.template_name,{"form":form})

class IndexView(View):
    template_name="index.html"

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    
class TaskCreateView(View):
    model=Task
    template_name="task-add.html"
    form_class=TaskForm

    def get(self,request,*args,**kwargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,"Todo added successfully")
            return redirect("index")
        messages.error(request,"Failed to create todo")
        return render(request,self.template_name,{"form":form})

class TaskListView(View):
    model=Task
    template_name="task-list.html"

    def get(self,request,*args,**kwargs):
        qs=Task.objects.filter(user=request.user)
        return render(request,self.template_name,{"tasks":qs})