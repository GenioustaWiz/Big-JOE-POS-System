from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *
urlpatterns = [
    path('', products_index, name='products_index'),
    path('add_item', add_item, name='add_item'),
    path('delete_item/<int:myid>/', delete_item, name='delete_item'),
    path('edit_item/<int:myid>/', edit_item, name='edit_item'),
    path('update_item/<int:myid>/', update_item, name='update_item'),

]