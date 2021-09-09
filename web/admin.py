from django.contrib import admin
from web.models import *
# Register your models here.



##for Category

class AdminCategory(admin.ModelAdmin):
    
    list_display=('Category_name','Super_Admin_Id')
 
class combineCategory(AdminCategory,CategorySearch):
    pass

#### for brands

class Adminbrand(admin.ModelAdmin):
    
    list_display=('image_tag','brandname','Category_Id')


 
class combinebrand(Adminbrand,BrandSearch):
    pass
     


##for subcategory


class AdminSubCategory(admin.ModelAdmin):
    
    list_display=('Category_Id','sub_Category_name')
 
class combineSubCategory(AdminSubCategory,subCategorySearch):
    pass


###for Items
class AdminItems(admin.ModelAdmin):
    
    list_display=('image_tag','Items_Name','Price','Stock','Category_Id','sub_Category_Id','Date_Time')

   

class combineItems(AdminItems,ItemSearch):
    pass


#####for customer order

class AdminOrders(admin.ModelAdmin):
    list_display=('firstname','lastname','city','phone','zipcode')


class combineOrders(AdminOrders,orderSearch):
    pass







admin.site.register(Category,combineCategory)
admin.site.register(Brand,combinebrand)
admin.site.register(Super_AdminAccount)
admin.site.register(subCategory,combineSubCategory)
admin.site.register(Items,combineItems)
admin.site.register(customerOrder,combineOrders)
