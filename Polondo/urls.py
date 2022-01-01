"""Polondo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from order import views as order_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name = 'home'),
    path('product/', include('products.urls'),  name= 'product'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('login/', user_views.login_form, name='login'),
    path('logout/', user_views.logout_func, name='logout'),
    path('signup/', user_views.signup_form, name='signup'),
    path('shopcart/', order_views.shopcart, name='shopcart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)