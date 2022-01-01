from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name = 'index'),
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
    
]
