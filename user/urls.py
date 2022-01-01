from django.urls import path, re_path
from . import views

#app_name = 'user'

urlpatterns = [
    path('', views.index, name='user_index'),

]