from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from shop.form import CustomUserForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    products=Products.objects.filter(trending=1)
    return render(request,'shop/index.html',{"products":products})


def register(request):
    form=CustomUserForm()
    if request.method== 'POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Succesfull")
            return redirect("/login")
    return render(request,'shop/register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully!")
                return redirect("/")
            else:
                messages.error(request,"Invalid Username or Password")
                return redirect("/login")


        return render(request,'shop/login.html')
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully!")
    return redirect("/")

  




def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{"category":category})

def collectionview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Products.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{"products":products,"category_name":name})
    else:
        messages.warning(request,"no such category found")
        return redirect("collections")

def productview(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Products.objects.filter(name=pname,status=0)):
            products=Products.objects.filter(name=pname).first()
            return render(request,"shop/products/product_details.html",{"products":products})
        else:
            messages.warning(request,"no such products found")
            return redirect("collections")
    else:
            messages.warning(request,"no such category found")
            return redirect("collections")
