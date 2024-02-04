# api_gateway/urls.py
from django.urls import path
from .views import index, save_data, view_data

urlpatterns = [
    path('', index, name='index'),
    path('save_data/', save_data, name='save_data'),
    path('view_data/', view_data, name='view_data'),
]
