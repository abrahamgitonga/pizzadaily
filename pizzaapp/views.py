from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import pizzaModel
# Create your views here.
def adminloginview(request):
    return render(request,"pizzaapp/adminlogin.html")

def authenticateadmin(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)

    #user exists
    if user is not None and user.username=="admin":
        login(request,user)
        return redirect('adminhomepage')

    #user doesnt exist
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('adminloginpage')

def adminhomepageview(request):
    context = {'pizzas': pizzaModel.objects.all()}
    return render(request,"pizzaapp/adminhomepage.html",context)

def logoutadmin(request):
    logout(request)
    return redirect('adminloginpage')

def addpizza(request):
    #code to add pizza
    name = request.POST['pizza']
    price = request.POST['price']
    pizzaModel(name = name, price = price).save()
    return redirect('adminhomepage')

def deletepizza(request,pizzapk):
    #code to delete pizza
    pizzaModel.objects.filter(id = pizzapk).delete()
    return redirect('adminhomepage')

def homepageview(request):
    return render(request,"pizzaapp/homepage.html")









