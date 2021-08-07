from django.db import models

# Create your models here.


class Super_AdminAccount(models.Model):

    SId = models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=255, default="First Name")
    Lname=models.CharField(max_length=255, default="Last Name")
    Email=models.EmailField(max_length=255, default="Email Name")
    Password=models.TextField(max_length=3000, default="Password ")
    ContactNo=models.CharField(max_length=100, default="Contact no")
    Profile= models.ImageField(upload_to='SuperAdmin/',default="SuperAdmin/dummy.jpg")
    def __str__(self):
        return self.Fname




class Category(models.Model):

    Category_Id = models.AutoField(primary_key=True)
    Category_name  = models.CharField(max_length=200, default="")
    Super_Admin_Id=models.ForeignKey(Super_AdminAccount , on_delete=models.SET_NULL,blank=True,null=True)
    

    def __str__(self):
        return self.Category_name



class Items(models.Model):

   
    Items_Name = models.CharField(max_length=255, default="")
    Stock = models.IntegerField(default=0)
    Product_Status = models.CharField(max_length=10, default="True")
    Date_Time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Category_Id = models.ForeignKey(Category , on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.Items_Name
    

