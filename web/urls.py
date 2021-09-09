from django.urls import path,include
from web.views import *

urlpatterns = [

#web urls  home
# path('',superadminlogin.as_view(),name="superadminlogin"),
path('superadminlogin',superadminlogin.as_view(),name="superadminlogin"),
path('Dashboard',Dashboard.as_view(),name="Dashboard"),
path('allCategory',allCategory.as_view(),name="allCategory"),
path('allSubCategory',allSubCategory.as_view(),name="allSubCategory"),
path('addCategory',addCategory.as_view(),name="addCategory"),
path('addSubCategory',addSubCategory.as_view(),name="addSubCategory"),
path('addItems',addItems.as_view(),name="addItems"),
path('editItems/<int:itemid>',editItems.as_view(),name="editItems"),
path('editCategory/<int:id>',editCategory.as_view(),name="editCategory"),
path('deleteCategory/<int:id>',deleteCategory.as_view(),name="deleteCategory"),
path('allItems',allItems.as_view(),name="allItems"),
path('logout',logout.as_view(),name="logout"),
path('deleteitem/<int:itemid>',deleteitem.as_view(),name="deleteitem"),



#####Clientside
path('',clientside.as_view(),name="clientside"),
path('contact',contact.as_view(),name="contact"),
path('brands/<int:id>',brands.as_view(),name="brands"),
path('products/<int:id>',products.as_view(),name="products"),
path('productview/<int:id>',productview.as_view(),name="productview"),
path('checkout/<int:id>/<int:quantity>',checkout.as_view(),name="checkout"),



]






