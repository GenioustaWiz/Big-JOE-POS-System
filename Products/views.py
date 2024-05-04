from re import S
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def products_index(request): #So that items can appear automatically on browser.
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 16) #adding paginator
    page_no = request.GET.get('page')
    item_list = paginator.get_page(page_no)
    context = {
        'item_list' : item_list
    }
    return render(request,'products.html', context)

def add_item(request):
    if request.method == 'POST' :
        name = request.POST['name']
        cost_price = request.POST['cost_price']
        selling_price = request.POST['selling_price']
        quantity = request.POST['quantity']
        product_type = request.POST['product_type']

        item= Item(name = name,cost_price = cost_price, selling_price = selling_price, quantity = quantity, product_type = product_type )
        item.save()

        messages.info(request, 'ITEM ADDED SUCCESSFULLY ')
        return redirect(products_index)
    else:
        pass

    item_list = Item.objects.all()
    context = {
        'item_list' : item_list
    }
    return render(request, 'products.html', context)

def delete_item(request, myid):
    item = Item.objects.get(id = myid)
    item.delete()
    messages.info(request, 'ITEM DELETED SUCCESSFULLY')
    return redirect(products_index)

def edit_item(request, myid):
    edit_item = Item.objects.get(id = myid)
    item_list = Item.objects.all()
    context = {
        'edit_item' : edit_item,
        'item_list' : item_list
    }
    return render(request, 'products.html', context)

def update_item(request, myid):
    item = Item.objects.get(id = myid)
    item.name = request.POST['name']
    item.cost_price = request.POST['cost_price']
    item.selling_price = request.POST['selling_price']
    item.quantity = request.POST['quantity']
    item.product_type = request.POST['product_type']
    item.save()
    messages.info(request, 'YOUR ITEM UPDATED SUCCESSFULLY')
    return redirect(products_index)