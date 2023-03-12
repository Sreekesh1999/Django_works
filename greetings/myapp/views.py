from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# localhost:8000/morning/
# get

class GoodmorningView(View):
    def get(self,request,*args,**kwargs):
        return render (request,"morning.html")

#localhost:8000/afternoon/
class GoodafternoonView(View):
    def get(self,request,*args,**kwargs):
        return render (request,"afternoon.html")
    
#localhost:800/evening/
class GoodeveningView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evening.html")