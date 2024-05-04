from django.urls import  path

from .views import *

urlpatterns= [
    path('', EmployeeListView.as_view(), name='employees'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('<pk>/update', UpdateView.as_view(), name='update'),
    path('<pk>/delete/', DeleteView.as_view(), name='delete'),
    
]