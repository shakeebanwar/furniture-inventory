from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from django.views import View
from rest_framework.response import Response
from passlib.hash import django_pbkdf2_sha256 as handler
from web.models import *

# Create your views here.

def checkAdminSession(self,request):
    if request.session.has_key('adminid'):
        return True

    else:
        return False



class superadminlogin(View):
    def get(self,request):
        return render(request,'superadmin/login.html')

    
    def post(self,request):
        try:
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

        except:
            return redirect('superadminlogin')


class logout(View):
    def get(self,request):
        try:
            del request.session['adminid']
            del request.session['adminname']
            del request.session['adminimg']
            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')




class Dashboard(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                categoeyCount = Category.objects.all().count()
                itemCount = Items.objects.all().count()
                return render(request,'superadmin/index.html',{'categoeyCount':categoeyCount,'itemCount':itemCount})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')



class allCategory(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Category.objects.all()
                return render(request,'superadmin/category.html',{'data':data})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')


class allSubCategory(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = subCategory.objects.all()
                return render(request,'superadmin/subcategory.html',{'data':data})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')

    

class deleteCategory(View):
    def get(self,request,id):
        try:

            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Category.objects.get(Category_Id = id).delete()
                return redirect('allCategory')

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')







class addCategory(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                return render(request,'superadmin/addcategory.html')

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')



    def post(self,request):
        try:
            name = request.POST['category']
            checkalreeady = Category.objects.filter(Category_name = name.lower())
            if not checkalreeady:
                fetchSuperadmin = Super_AdminAccount.objects.get(SId = request.session['adminid'])
                createobj = Category(Category_name = name.lower() ,Super_Admin_Id = fetchSuperadmin)
                createobj.save()
                return redirect('allCategory')
            
            else:
                return render(request,'superadmin/addcategory.html',{'status':True})

        except:
            return redirect('superadminlogin')


class addSubCategory(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Category.objects.all()
                return render(request,'superadmin/addsubcategory.html',{'data':data})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')


    def post(self,request):
        try:
        

            name = request.POST['subcategory']
            categoryid = request.POST['category']
            checkalreeady = subCategory.objects.filter(sub_Category_name = name.lower())
            if not checkalreeady:
                categoryObj = Category.objects.get(Category_Id = categoryid)
                createobj = subCategory(sub_Category_name = name.lower(),Category_Id = categoryObj )
                createobj.save()
                return redirect('allSubCategory')
            
            else:
                data = Category.objects.all()
                return render(request,'superadmin/addsubcategory.html',{'status':True,'data':data})

        except:
            return redirect('superadminlogin')




        
class editCategory(View):
    def get(self,request,id):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Category.objects.get(Category_Id = id)
                return render(request,'superadmin/editcategory.html',{'data':data})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')

    def post(self,request,id):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                name = request.POST['category']
                data = Category.objects.filter(Category_name = name)
                if not data:
                    data = Category.objects.get(Category_Id = id)
                    data.Category_name = name
                    data.save()
                
                
                return redirect('allCategory')

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')

        
     

     

    


class allItems(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Items.objects.all()
                return render(request,'superadmin/items.html',{'data':data})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')



class addItems(View):
    def get(self,request):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                data = Category.objects.all()
                dataSub = subCategory.objects.all()
                return render(request,'superadmin/addItems.html',{'data':data,'dataSub':dataSub})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')



    def post(self,request):
        try:
            name = request.POST['name']
            stock = request.POST['stock']
            category = request.POST['category']
            price = request.POST['price']
            subcategory = request.POST['subcategory']
            subcategory = request.POST['subcategory']
            desc = request.POST['desc']

            img = request.FILES['img']
            checkalreeady = Items.objects.filter(Items_Name = name.lower())
            if not checkalreeady:
                categoryObj = Category.objects.get(Category_Id = category)
                subcategoryObj = subCategory.objects.get(sub_Category_Id = subcategory)
                createobj = Items(Items_Name = name.lower() ,Stock = stock,Category_Id = categoryObj,sub_Category_Id = subcategoryObj,Price = price,productimg = img,Description = desc)
                createobj.save()
                return redirect('allItems')

            else:
                data = Category.objects.all()
                return render(request,'superadmin/addItems.html',{'data':data,'status':True})

        except:
            return redirect('superadminlogin')


class editItems(View):
    def get(self,request,itemid):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                itemObj = Items.objects.get(id = itemid)
                data = Category.objects.all()
                return render(request,'superadmin/edititems.html',{'data':data,'itemObj':itemObj})

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')

    def post(self,request,itemid):
        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
                name = request.POST['name']
                stock = request.POST['stock']
                category = request.POST['category']
                price = request.POST['price']
                categoryObj = Category.objects.get(Category_Id = category)
                itemObj = Items.objects.get(id = itemid)
                checkalready =  Items.objects.filter(Items_Name = name)
                if not checkalready:
                    itemObj.Items_Name = name
                itemObj.Stock = stock
                itemObj.Category_Id = categoryObj
                itemObj.Price = price
                itemObj.save()
                return redirect('allItems')

            return redirect('superadminlogin')


        except:
            return redirect('superadminlogin')

    
        
class deleteitem(View):
    def get(self,request,itemid):
  

        try:
            sessionhandle = checkAdminSession(self,request)
            if sessionhandle:
               
                itemObj = Items.objects.get(id = itemid).delete()
                return redirect('allItems')

            return redirect('superadminlogin')

        except:
            return redirect('superadminlogin')




###Client side
class clientside(View):
    def get(self,request):
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()
        return render(request,'clientside/index.html',{'categoryObj':categoryObj,'brandObj':brandObj})



class contact(View):
    def get(self,request):
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()
        return render(request,'clientside/Contact.html',{'categoryObj':categoryObj,'brandObj':brandObj})


class brands(View):
    def get(self,request,id):
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()
        specificBrand  = Brand.objects.filter(Category_Id = id)
        return render(request,'clientside/brands.html',{'categoryObj':categoryObj,'brandObj':brandObj,'specificBrand':specificBrand})

class products(View):
    def get(self,request,id):
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()
        return render(request,'clientside/products.html',{'categoryObj':categoryObj,'brandObj':brandObj})



class productview(View):
    def get(self,request):
        return render(request,'clientside/productview.html')


class checkout(View):
    def get(self,request):
        return render(request,'clientside/checkout.html')



   