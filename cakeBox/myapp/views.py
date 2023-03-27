from django.shortcuts import render,redirect
from django import forms
from django.views.generic import View
from myapp.models import Cakes

# Create your views here.
class CakeForm(forms.Form):
    name=forms.CharField()
    flavour=forms.CharField()
    price=forms.IntegerField()
    shape=forms.CharField()
    weight=forms.CharField()
    layer=forms.CharField()
    descriptions=forms.CharField()

class CakeBoxCreateView(View):
    def get(self,request,*args,**kwargs):
        form=CakeForm()
        return render(request,"cakebox-add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=CakeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Cakes.objects.create(**form.cleaned_data)
            return redirect("cakebox-list")
        return render(request,"cakebox-add.html",{"cake":form})
    
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
        return redirect("cakebox-list")
