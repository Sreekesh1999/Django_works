from django.shortcuts import render,redirect
from django import forms
from django.views.generic import View
from tasks.models import Todos
from django.contrib import messages

class TodoForm(forms.Form):
    task_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        return render(request,"todo-add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todos.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"Todo has been created successfully")
            return redirect("todo-list")
        messages.error(request,"Failed to create Todo")
        return render(request,"todo-add.html",{"form":form})

class TodoListView(View):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=False,user=request.user).order_by("-date")
        return render(request,"todo-list.html",{"todos":qs})
    
class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Todos.objects.get(id=id)
        return render(request,"todo-detail.html",{"todo":qs})
    
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.get(id=id).delete()
        messages.success(request,"Todo has been removed successfully")
        return redirect("todo-list")
    
class TaskEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Todos.objects.filter(id=id).update(status=True)
        messages.success(request,"Todo has been updated successfully")
        return redirect("todo-list")
    
class TodoCompletedView(View):
    def get(self,request,*args,**kwargs):
        qs=Todos.objects.filter(status=True)
        return render(request,"todo-completed.html",{"completed":qs})
