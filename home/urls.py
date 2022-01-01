from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='about'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
]
