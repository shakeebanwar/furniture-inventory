from django.urls import path,include
from web.views import *

urlpatterns = [

#web urls  home
path('superadminlogin',superadminlogin.as_view(),name="superadminlogin"),
path('Dashboard',Dashboard.as_view(),name="Dashboard"),
path('allCategory',allCategory.as_view(),name="allCategory"),
path('addCategory',addCategory.as_view(),name="addCategory"),
path('addItems',addItems.as_view(),name="addItems"),
path('editItems/<int:itemid>',editItems.as_view(),name="editItems"),
path('editCategory/<int:id>',editCategory.as_view(),name="editCategory"),
path('deleteCategory/<int:id>',deleteCategory.as_view(),name="deleteCategory"),
path('allItems',allItems.as_view(),name="allItems"),
path('logout',logout.as_view(),name="logout"),
path('deleteitem/<int:itemid>',deleteitem.as_view(),name="deleteitem"),
]






