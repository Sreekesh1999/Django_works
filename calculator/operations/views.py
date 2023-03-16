from django.shortcuts import render
from django.views.generic import View

# Create your views here.
# Localhost:8000/add
# Get
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1+n2
        print(res)
        return render(request,"add.html",{"result":res})
    

class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1-n2
        print(res)
        return render(request,"sub.html",{"result":res})
    
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1*n2
        print(res)
        return render(request,"mul.html",{"result":res})
    
class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        res=n1/n2
        print(res)
        return render(request,"div.html",{"result":res})

class CubeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"cube.html")
    
    def post(self,request,*args,**kwargs):
        n1=int(request.POST.get("num"))
        res=n1**3
        print(res)
        return render(request,"cube.html",{"result":res})

class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    
    def post(self,request,*args,**kwargs):
        n=int(request.POST.get("num"))
        fact = 1

        for i in range(1,(n+1)):
            fact=fact*i
        return render(request,"fact.html",{"result":fact})
    
class PrimenumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        return render(request,"prime.html")
    
class ArmstrongView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"armstrong.html")
    
    def post(self,request,*args,**kwargs):
        num=int(request.POST.get("num"))
        sum=0
        original=num
        while(num!=0):
            digit = num % 10
            sum = sum +(digit**3)
            num=num//10
        result=original==sum
        return render(request,"armstrong.html",{"res":result})
    
class PalindromeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"palindrome.html")
    
    def post(self,request,*args,**kwargs):
        string=request.POST.get("string")
        rev=string[::-1]
        res=rev==string
        return render(request,"palindrome.html",{"result":res})
    
class EvennumbersView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"evennumber.html")
    
    def post(self,request,*args,**kwargs):
        num1=int(request.POST.get("num1"))
        num2=int(request.POST.get("num2"))
        even_numbers = [num for num in range(num1,num2+1) if num % 2 == 0]
        return render(request,"evennumber.html",{"result":even_numbers})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")
    
class HealthyView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"health.html")
    
    def post(self,request,*args,**kwargs):
        tummy_size=int(request.POST.get("tsize"))
        buttock_size=int(request.POST.get("bsize"))
        gender=request.POST.get("gender")
        # print(tummy_size)
        # print(buttock_size)
        # print(gender)
        bmi=tummy_size/buttock_size
        bmi=round(bmi,2)
        context={"Gender":"","Risk":"","Shape":"","bmi":bmi}

        if gender=="male":
            if bmi<=.95:
                context["Gender"]="Male"
                context["Risk"]="Low"
                context["Shape"]="Pear"
            elif bmi>=.96 and bmi<= 1:
                context["Gender"]="Male"
                context["Risk"]="Medium"
                context["Shape"]="Avocado"
            else:
                context["Gender"]="Male"
                context["Risk"]="High"
                context["Shape"]="Apple"
        else:
            if bmi<=.80:
                context["Gender"]="Female"
                context["Risk"]="Low"
                context["Shape"]="Pear"
            elif bmi>=.96 and bmi<=1:
                context["Gender"]="Female"
                context["Risk"]="Medium"
                context["Shape"]="Avocado"
            else:
                context["Gender"]="Female"
                context["Risk"]="High"
                context["Shape"]="Apple"

        return render(request,"health.html",context)

    