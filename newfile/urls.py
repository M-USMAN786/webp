from django.contrib import admin
from django.urls import path
from newfile import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('Usman728/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path("search",views.search_home, name="search"),
    path("poetry/search",views.search_poetry, name="search"),
    path("save_contact_form",views.save_contact_form, name='save_contact_form'),
    path('contact',views.contact,name='contact'),
    path('poetry',views.poetry,name='poetry'),
    path('android_apps',views.android_apps,name='AndroidApps'),
]

if settings.DEBUG:
 urlpatterns+=static(settings.MEDIA_URLS,document_root=settings.MEDIA_ROOT)