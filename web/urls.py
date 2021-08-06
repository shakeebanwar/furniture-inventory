from django.urls import path,include
from web.views import *

urlpatterns = [

#web urls  home
path('superadminlogin',superadminlogin.as_view()),
path('Dashboard',Dashboard.as_view()),
path('allCategory',allCategory.as_view()),
path('allItems',allItems.as_view()),

]






