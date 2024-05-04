from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView  
from .models import  *
from .forms import CustomUserCreationForm
from django.core.paginator import Paginator

# Create your views here.
""" def EmployeeListView(request): #So that items can appear automatically on browser.
    users = CustomUser.objects.all()
    
    context = {
        'users' : users
    }
    return render(request,'users/register_View.html', context)
"""
class EmployeeListView(ListView):
    model = CustomUser
    template_name = 'users/register_View.html'
    context_object_name = 'employees'
    paginate_by =100
    page_kwarg = 'page'
    ordering = ['id']


class SignupView(CreateView):
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('employees') 
    template_name = 'users/register_View.html' 
"""
def SignupView(request):
    
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        print('Ayeeeeee')
        
        form.save()
        return redirect('employees')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    
    return render(request, 'users/register_View.html', context )
"""
class UpdateView(UpdateView):
    model = CustomUser #Very Important
    form_class = CustomUserCreationForm
    template_name = 'users/register_View.html' 
    success_url = reverse_lazy('employees')

class DeleteView(DeleteView):
    #Specify the model yu want to use       
    model = CustomUser #Very Important
    template_name = 'users/delete.html' 
    success_url = reverse_lazy('employees')