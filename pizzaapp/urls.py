
from django.contrib import admin
from django.urls import path
from .views import adminloginview,adminhomepageview,authenticateadmin, customerwelcomeview, logoutadmin,addpizza,deletepizza,homepageview,signupuser, userauthenticate, userloginview, userlogout
urlpatterns = [
    path('admin/', adminloginview,name = 'adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage',adminhomepageview,name = 'adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('',homepageview,name = 'homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview,name= 'userloginpage'),
    path('customer/welcome/',customerwelcomeview, name= 'customerpage'),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/',userlogout)


]
