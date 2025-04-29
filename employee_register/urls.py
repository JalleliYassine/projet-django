from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form,name='employee_insert'),#name is for get and post req for insert
    path('<int:id>/',views.employee_form,name='employee_update'), #name is for get and post req for update
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.employee_list,name='employee_list') #name is for get to retrieve 
    
]
