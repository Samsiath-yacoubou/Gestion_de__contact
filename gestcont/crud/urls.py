from django.urls import path
from crud.views import contact_create,contact_delete,contact_list,contact_update

urlpatterns = [
    path('',contact_list,name = 'contact_list'),
    path('create/',contact_create,name='contact_create'),
    path('update/<int:pk>/', contact_update, name='contact_update'),
    path('delete/<int:pk>/', contact_delete, name='contact_delete'),
]