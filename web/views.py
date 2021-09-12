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
        if not request.session.has_key('userid'):
            itemObj = Items.objects.filter(brandid = id)
            if itemObj:
                topRatedStatus = 'true'
            else:
                topRatedStatus = 'false'

            return render(request,'clientside/products.html',{'categoryObj':categoryObj,'brandObj':brandObj,'itemObj':itemObj,'topRatedStatus':topRatedStatus})

        else:
            itemObj = Items.objects.filter(brandid = id)
            if itemObj:
                topRatedStatus = 'true'
            else:
                topRatedStatus = 'false'

            recomandedList = list()
            recomanded = customerOrder.objects.filter(userid = request.session['userid'])
           
            for j in recomanded:
                recomandedList.append(j.productid.Category_Id.Category_Id)

            if len(recomandedList) > 0:
                recomandedStatus = 'true'

            else:
                recomandedStatus = 'false'


            recomedObj = Items.objects.filter(Category_Id__in = recomandedList)
            return render(request,'clientside/products.html',{'categoryObj':categoryObj,'brandObj':brandObj,'itemObj':itemObj,'recomanded':recomedObj,'recomandedStatus':recomandedStatus,'topRatedStatus':topRatedStatus})
         



class productview(View):
    def get(self,request,id):
        itemObj = Items.objects.get(id = id)
        return render(request,'clientside/productview.html',{'itemObj':itemObj})


class checkout(View):
    def get(self,request,id,quantity):
        if request.session.has_key('userid'):
            categoryObj = Category.objects.all()
            brandObj = Brand.objects.all()
            itemObj = Items.objects.get(id = id)
            return render(request,'clientside/checkout.html',{'itemObj':itemObj,'quantity':quantity,'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':'hide'})

        else:
            return redirect('signup')

    def post(self,request,id,quantity):

        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        streetAddress = request.POST['street-address-1']
        town = request.POST['town']
        phone = request.POST['phone']
        order_notes = request.POST['order_notes']
        itemObj = Items.objects.get(id = id)
        if itemObj.Stock == 0:
            
            return render(request,'clientside/checkout.html',{'itemObj':itemObj,'quantity':quantity,'categoryObj':categoryObj,'brandObj':brandObj,'redirect':False,'messagestatus':'warning','message':'Sorry Your Order is out of stock'})

        elif itemObj.Stock < quantity:
            return render(request,'clientside/checkout.html',{'itemObj':itemObj,'quantity':quantity,'categoryObj':categoryObj,'brandObj':brandObj,'redirect':False,'messagestatus':'warning','message':f'Only {itemObj.Stock} Quantity is available'})






        userObj = signup.objects.get(id= request.session['userid'])
        data = customerOrder(firstname=firstname,lastname=lastname,streetAdress=streetAddress,city=town,ordernote=order_notes,productid=itemObj,userid=userObj,quantity = quantity,phone=phone)
        data.save()
        itemObj.Stock = itemObj.Stock - quantity
        itemObj.save()


        return render(request,'clientside/checkout.html',{'itemObj':itemObj,'quantity':quantity,'categoryObj':categoryObj,'brandObj':brandObj,'redirect':'True','messagestatus':'success','message':'Your Order has been Book Successfully'})
   




class usersignup(View):
    def get(self,request):
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()
        return render(request,'clientside/auth.html',{'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':'hide'})


    def post(self,request):
       
        email = request.POST['email']
        password = request.POST['password']
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()

        ##check if already exist

        existObj = signup.objects.filter(Email = email)
        if not existObj:
            signup(Email = email,Password = handler.hash(password)).save()
            return render(request,'clientside/auth.html',{'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':"success",'message':"Account Created Successfully"})

        else:
            return render(request,'clientside/auth.html',{'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':"warning",'message':"Email Already Exist"})



class login(View):
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        categoryObj = Category.objects.all()
        brandObj = Brand.objects.all()

        fetchUsernObj = signup.objects.filter(Email = email)
        if fetchUsernObj and handler.verify(password,fetchUsernObj[0].Password):
            request.session['userid'] = fetchUsernObj[0].id
            return render(request,'clientside/auth.html',{'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':"success",'message':"Login SuccessFully",'redirect':True})



        else:
            return render(request,'clientside/auth.html',{'categoryObj':categoryObj,'brandObj':brandObj,'messagestatus':"warning",'message':"Invalid Credential"})



