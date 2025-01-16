"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 

    path('', views.home, name="Welcome"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('signupaction/', views.signupaction, name="signupaction"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('userhome/', views.userhome, name="userhome"),
    path('userlogout/', views.userlogout, name="userlogout"),



    path('addcategory/', views.addcategory, name="addcategory"),
    path('addcataction/', views.addcataction, name="addcataction"),
    path('additem/', views.additem, name="additem"),
    path('additemaction/', views.additemaction, name="additemaction"),
    path('viewproducts/', views.viewproducts, name="viewproducts"),
    path('addstocks/', views.addstocks, name="addstocks"),
    path('manageaddress/', views.manageaddress, name="manageaddress"),
    path('deleteaddress/', views.deleteaddress, name="deleteaddress"),
    path('updateaddress/', views.updateaddress, name="updateaddress"),
    path('addaddr/', views.addaddr, name="addaddr"),
    
    path('profile/', views.profile, name="profile"),
    path('uviewproducts/<str:cid>/', views.uviewproducts, name="uviewproducts"),
    path('viewsingle/<str:pid>/', views.viewsingle, name="viewsingle"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('cartview/', views.cartview, name="cartview"),
    path('cartdelete/<str:op>/', views.cartdelete, name="cartdelete"),
    path('payment/', views.payment, name="payment"),
    path('sellerlogin/', views.slogin, name="sellerlogin"),
    path('sellersignup/', views.sellersignup, name="sellersignup"),
    path('viewsellers/', views.viewsellers, name="viewsellers"),
    path('newsellers/', views.newsellers, name="newsellers"),
    path('sellerstz/', views.sellerstz, name="sellerstz"),
    path('slogin/', views.slogin, name="slogin"),
    
    path('shome/', views.shome, name="shome"),
    path('slogout/', views.slogout, name="slogout"),
    path('viewsellers/', views.viewsellers, name="viewsellers"),
    path('vieworders/', views.vieworders, name="vieworders"),
    path('uvieworders/', views.uvieworders, name="uvieworders"),
    path('accept/', views.accept, name="accept"),
    path('allot/', views.allot, name="allot"),  
    path('addcoupons/', views.addcoupons, name="addcoupons"),
    path('deletecode/', views.deletecode, name="deletecode"),
    path('terms/', views.terms, name="terms"),
    path('faqs/', views.faqs, name="faqs"),
    path('aboutus/', views.aboutus, name="aboutus"),


    path('couponverify/', views.couponverify, name="couponverify"),  
    

    
        
    path('rpay/', views.rpay, name="rpay"),
    path('search/', views.search, name="search"),

    

    

     
]
