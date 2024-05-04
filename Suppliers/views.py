from re import S
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def supplier_index(request): #So that items can appear automatically on browser.
   # messages.set_level(request, None) #For reseting message display on html
    item_list = supplier.objects.all()
    paginator = Paginator(item_list, 16) #adding paginator
    page_no = request.GET.get('page')
    item_list = paginator.get_page(page_no)
    context = {
        'item_list' : item_list
    }
    return render(request,'supplier.html', context)

def add_s(request):
    if request.method == 'POST' :
        name = request.POST['name']
        company = request.POST['company']
        content_supplied = request.POST['content_supplied']
        phone = request.POST['phone']
        email = request.POST['email']

        item= supplier(name = name, company = company, content_supplied = content_supplied, phone = phone, email = email )
        item.save()

        messages.info(request, 'ITEM ADDED SUCCESSFULLY ')
        return redirect('supplier_index')
    else:
        pass

    item_list = supplier.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'supplier.html', context)

def delete_s(request, myid):
    item = supplier.objects.get(id = myid)
    item.delete()
    messages.info(request, 'ITEM DELETED SUCCESSFULLY')
    return redirect(supplier_index)

def edit_s(request, myid):
    edit_s= supplier.objects.get(id = myid)
    item_list = supplier.objects.all().order_by('id')
    context = {
        'edit_s' : edit_s,
        'item_list' : item_list,
    }
    return render(request, 'supplier.html', context)

def update_s(request, myid):
    item = supplier.objects.get(id = myid)
    item.name = request.POST['name']
    item.company = request.POST['company']
    item.content_supplied = request.POST['content_supplied']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.save()
    messages.info(request, 'YOUR ITEM UPDATED SUCCESSFULLY')
    return redirect(supplier_index)