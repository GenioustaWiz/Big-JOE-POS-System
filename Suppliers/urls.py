from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
urlpatterns = [
    path('', supplier_index, name='supplier_index'),
    path('add_s', add_s, name='add_s'),
    path('delete_s/<int:myid>/', delete_s, name='delete_s'),
    path('edit_s/<int:myid>/', edit_s, name='edit_s'),
    path('update_s/<int:myid>/', update_s, name='update_s'),

]