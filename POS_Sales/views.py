from django.shortcuts import render

# Create your views here.
def pos_index(request):

    return render(request, 'pos.html')