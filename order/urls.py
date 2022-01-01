from django.urls import path, re_path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
]