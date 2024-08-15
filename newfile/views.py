from django.shortcuts import render
from django.core.paginator import Paginator
from newfile.models import new_upload
from newfile.models import contact_form_data
from newfile.models import poetry_model
from newfile.models import android_apps_model

from django.core.paginator import Paginator
# Create your views here.
def home(request):
    # for pagination
    new_upload_data=new_upload.objects.all()
    paginator=Paginator(new_upload_data,5)
    page_number=request.GET.get('page')
    new_puload_data_final=paginator.get_page(page_number)
    total_pages=new_puload_data_final.paginator.num_pages
    
    
    data={
        'NewUploadData':new_puload_data_final,
        'last_page':total_pages,
        # 'next_page':new_puload_data_final_int
    }
    return render(request,'home.html',data)
def search_home(request):
    # search
    query=request.GET['search']
    serached_posts=new_upload.objects.filter(file_name__icontains=query)
    searched_data={
        'NewUploadData':serached_posts,
    }
    return render(request,'home.html',searched_data)

def contact(request):
    return render(request,'contact.html')

def save_contact_form(request):
    response=''
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data_contact_form=contact_form_data(name=name,email=email,message=message)
        data_contact_form.save()
        response='The message has been sent.'
    return render(request,'contact.html',{'response':response})




def poetry(request):
    poetry_dat=poetry_model.objects.all()
    poetry_paginator=Paginator(poetry_dat,2)
    page_number_poetry=request.GET.get('page')
    poetry_data_final=poetry_paginator.get_page(page_number_poetry)
    total_pages=poetry_data_final.paginator.num_pages
    data={
        'poetry_data':poetry_data_final,
        'last_page':total_pages
    }

    return render(request,'poetry.html', data)

def search_poetry(request):
    response='Search Results:'
    query=request.GET['search']
    serached_posts=poetry_model.objects.filter(poet_name__icontains=query)
    searched_data={
        'poetry_data':serached_posts,
        'response':response,
    }
    return render(request,'poetry.html',searched_data)

def android_apps(request):
    new_android_apps=android_apps_model.objects.all()
    paginator=Paginator(new_android_apps,1)
    page_number=request.GET.get('page')
    new_puload_data_final=paginator.get_page(page_number)
    total_pages=new_puload_data_final.paginator.num_pages
    
    
    data={
        'NewUploadData':new_puload_data_final,
        'last_page':total_pages,
        # 'next_page':new_puload_data_final_int
    }
    return render(request,'android_apps.html',data)



