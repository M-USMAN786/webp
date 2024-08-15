from django.db import models

# Create your models here.
class new_upload(models.Model):
    file_name=models.CharField(max_length=150,default=None)
    file_ver=models.CharField(max_length=150,default=None)
    file_required_size=models.CharField(max_length=150,default=None)
    file_size=models.CharField(max_length=150,default=None)
    file_category=models.CharField(max_length=150,default=None)
    file_source=models.CharField(max_length=150,default=None)
    file_link=models.CharField(max_length=1000,default=None)
    file_img=models.FileField(upload_to="", max_length=500,default='none',null='true')

class contact_form_data(models.Model):
    name=models.CharField(max_length=100,null=None)
    email=models.EmailField(max_length=354,null=None)
    message=models.TextField(null=None)    

class poetry_model(models.Model):
    poetry=models.TextField(default=None)
    poet_name=models.CharField(max_length=100)

class android_apps_model(models.Model):
    app_img=models.FileField(upload_to="",default=None,null=True, max_length=500)
    app_name=models.CharField(max_length=200)
    app_ver=models.CharField(max_length=200)
    app_link=models.CharField(max_length=500)
    app_source=models.CharField(max_length=200)
    app_category=models.CharField(max_length=200)
    app_size=models.CharField(max_length=200)
