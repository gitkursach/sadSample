from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('add_line/', add_line, name='add_line'),
    path('edit_line/<int:pk>/', edit_line, name='edit_line'),
    path('delete_line/<int:pk>/', delete_line, name='delete_line'),

]