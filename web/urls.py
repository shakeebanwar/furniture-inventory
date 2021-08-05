from django.urls import path,include
from web.views import *

urlpatterns = [

#web urls  home
path('superadminlogin',superadminlogin.as_view()),

]






