from django.contrib import admin
from newfile.models import new_upload, contact_form_data, poetry_model, android_apps_model
# Register your models here.
class new_upload_admin(admin.ModelAdmin):
    list_display=('file_name','file_link','file_img','file_ver','file_category','file_source','file_required_size','file_size')
admin.site.register(new_upload,new_upload_admin)

class contact_form_data_admin(admin.ModelAdmin):
    list_display=('name','email','message')
admin.site.register(contact_form_data,contact_form_data_admin)

class poetry_admin(admin.ModelAdmin):
    list_display=('poetry','poet_name')
admin.site.register(poetry_model, poetry_admin)

class android_apps_admin(admin.ModelAdmin):
    list_display=('app_img','app_name','app_ver','app_link','app_source','app_category','app_size')
admin.site.register(android_apps_model, android_apps_admin)
