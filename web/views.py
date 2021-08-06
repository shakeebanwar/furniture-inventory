from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from passlib.hash import django_pbkdf2_sha256 as handler
from web.models import *

# Create your views here.
class superadminlogin(View):
    def get(self,request):
        return render(request,'superadmin/login.html')

    
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        fetchAdminObj = Super_AdminAccount.objects.filter(Email = email)
        if fetchAdminObj and handler.verify(password,fetchAdminObj[0].Password):
            request.session['adminid'] = fetchAdminObj[0].SId
            request.session['adminname'] = fetchAdminObj[0].Fname + fetchAdminObj[0].Lname
            request.session['adminimg'] = fetchAdminObj[0].Profile.url
            return redirect('Dashboard')
            

        else:
            return render(request,'superadmin/login.html',{'status':True})


class Dashboard(View):
    def get(self,request):
        categoeyCount = Category.objects.all().count()
        itemCount = Items.objects.all().count()
        return render(request,'superadmin/index.html',{'categoeyCount':categoeyCount,'itemCount':itemCount})



class allCategory(View):
    def get(self,request):
        data = Category.objects.all()
        return render(request,'superadmin/category.html',{'data':data})



class allItems(View):
    def get(self,request):
        data = Items.objects.all()
        return render(request,'superadmin/items.html',{'data':data})

      