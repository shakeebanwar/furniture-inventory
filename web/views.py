from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from passlib.hash import django_pbkdf2_sha256 as handler

# Create your views here.
class superadminlogin(APIView):
    def get(self,request):
        return HttpResponse("OK")