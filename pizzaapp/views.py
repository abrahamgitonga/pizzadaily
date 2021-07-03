from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import pizzaModel,customerModel,orderModel
from django.contrib.auth.models import User 
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

def signupuser(request):
    username = request.POST['username']
    password = request.POST['password']
    telephone = request.POST['telephone']
    
    #if user already exists
    if User.objects.filter(username = username).exists():
        messages.add_message(request,messages.ERROR,"User already exists")
        return redirect('homepage')
    


    #new user 
    User.objects.create_user(username = username, password = password).save()
    lastobject = len(User.objects.all())-1
    customerModel(userid = User.objects.all()[int(lastobject)].id,telephone = telephone).save()
    messages.add_message(request,messages.ERROR,"user registration success")
    return redirect('homepage')

def userloginview(request):
    return render(request,"pizzaapp/userlogin.html")    

def userauthenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username = username,password = password)

    #user exists
    if user is not None:
        login(request,user)
        return redirect('customerpage')

    #user doesnt exist
    if user is None:
        messages.add_message(request,messages.ERROR,"Invalid Credentials")
        return redirect('userloginpage')

    

def customerwelcomeview(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    context = {'username': username,'pizzas': pizzaModel.objects.all()}
    return render(request,'pizzaapp/customerpage.html',context)

def userlogout(request):
    logout(request)
    return redirect('userloginpage')

def placeorder(request):
    if not request.user.is_authenticated:
        return redirect('userloginpage')
    username = request.user.username
    telephone = customerModel.objects.filter(userid = request.user.id)[0].telephone
    address = request.POST['address']
    ordereditems = ""

    for pizza in pizzaModel.objects.all():
        pizzaid = pizza.id
        name = pizza.name
        price = pizza.price
        quantity = request.POST.get(str(pizzaid)," ")
        if str(quantity)!="0" and str(quantity)!="":

            ordereditems = ordereditems + name +"  " + "price : "+ str(int(quantity)*int(price)) +" "+ "quantity : " + quantity + "  "

    orderModel(username = username,telephone = telephone,address = address,ordereditems = ordereditems).save()
    messages.add_message(request,messages.ERROR,"order placement success")
    return redirect('customerpage')

def usersorders(request):
    orders = orderModel.objects.filter(username = request.user.username)
    context = {'orders' : orders}
    return render(request,'pizzaapp/usersorders.html',context)



    


