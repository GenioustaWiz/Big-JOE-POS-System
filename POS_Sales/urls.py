from django.urls import path
from .views import *
urlpatterns = [
    path('', pos_index, name = 'pos_index' )
]