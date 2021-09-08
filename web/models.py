from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe

capitalizeFirstChar = lambda s: s[:1].upper() + s[1:]

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
    Category_name  = models.CharField(max_length=200, default="",unique=True)
    Super_Admin_Id=models.ForeignKey(Super_AdminAccount , on_delete=models.SET_NULL,blank=True,null=True)
    

    def __str__(self):
        return self.Category_name

    # The save method to convert your text "MY naME is jOHN" to "My name is john"

    def save(self, force_insert=False, force_update=False):
        self.Category_name = self.Category_name.lower()
        self.Category_name = capitalizeFirstChar(self.Category_name)

        # If the name already exists
        if not Category.objects.filter(Category_name__iexact=self.Category_name).exists():
            super(Category, self).save(force_insert, force_update)

##### for searching purpose#####

class CategorySearch(admin.ModelAdmin):
    search_fields = ['Category_name']



class Brand(models.Model):
    brandname  = models.CharField(max_length=200, default="",unique=True)
    Category_Id=models.ForeignKey(Category , on_delete=models.SET_NULL,blank=True,null=True)
    brandlogo= models.ImageField(upload_to='brand/',default="product/dummy.jpg")

    def __str__(self):
        return self.brandname


    ### Display the image in model
    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.brandlogo.url))

    image_tag.short_description = 'Image'


    # The save method to convert your text "MY naME is jOHN" to "My name is john"

    def save(self, force_insert=False, force_update=False):
        self.brandname = self.brandname.lower()
        self.brandname = capitalizeFirstChar(self.brandname)

        # If the name already exists
        if not Brand.objects.filter(brandname__iexact=self.brandname).exists():
            super(Brand, self).save(force_insert, force_update)




##### for searching purpose#####

class BrandSearch(admin.ModelAdmin):
    search_fields = ['brandname']



class subCategory(models.Model):

    sub_Category_Id = models.AutoField(primary_key=True)
    sub_Category_name  = models.CharField(max_length=200, default="",unique=True)
    Category_Id=models.ForeignKey(Category , on_delete=models.SET_NULL,blank=True,null=True)

  
    
    def __str__(self):
        return self.sub_Category_name


    # The save method to convert your text "MY naME is jOHN" to "My name is john"

    def save(self, force_insert=False, force_update=False):
        self.sub_Category_name = self.sub_Category_name.lower()
        self.sub_Category_name = capitalizeFirstChar(self.sub_Category_name)

        # If the name already exists
        if not subCategory.objects.filter(sub_Category_name__iexact=self.sub_Category_name).exists():
            super(subCategory, self).save(force_insert, force_update)




##### for searching purpose#####

class subCategorySearch(admin.ModelAdmin):
    search_fields = ['sub_Category_name']


class Items(models.Model):

   
    Items_Name = models.CharField(max_length=255, default="")
    Stock = models.IntegerField(default=0)
    Price = models.IntegerField(default=0)
    Description = models.TextField(default="")
    Product_Status = models.CharField(max_length=10, default="True")
    Date_Time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    Category_Id = models.ForeignKey(Category , on_delete=models.SET_NULL,blank=True,null=True)
    sub_Category_Id = models.ForeignKey(subCategory , on_delete=models.SET_NULL,blank=True,null=True)
    productimg= models.ImageField(upload_to='product/',default="product/dummy.jpg")

    def __str__(self):
        return self.Items_Name

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.productimg.url))

    image_tag.short_description = 'Image'
        

##### for searching purpose#####

class ItemSearch(admin.ModelAdmin):
    search_fields = ['Items_Name','Stock','Price','Description','Product_Status']


