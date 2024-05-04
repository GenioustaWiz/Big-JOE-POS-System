from django.shortcuts import render
#from main_page.models import Main

# Create your views here.
def main_index(request):
    
    return render(request, 'index_web.html',)
