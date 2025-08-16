from django.contrib import admin
from django.urls import path

from contatos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.contacts, name='principal'),
    path('contacts/', views.contacts, name='contacts'),
    path('new_contact/', views.new_contact, name='new_contact'),
    path('validate_new_contact/', views.validate_new_contact, name='validate_new_contact'),
    path('view_contact/<int:id>/', views.view_contact, name='view_contact'),
    path('edit_contact/<int:id>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
    path('security/', views.security, name='security'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('validate_login/', views.validate_login, name='validate_login'),
]
