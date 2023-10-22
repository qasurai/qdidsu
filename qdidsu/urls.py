"""qdidsu URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path
from collect import views as c_v
from .settings import STATIC_ROOT
from django.views import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/', c_v.reg),
    path('list/', c_v.getlist),
    path('login/', c_v.login),
    path('logout/', c_v.logout),
    path('view/<int:uid>/', c_v.viewp),
    path('delgl/<int:uid>/', c_v.delgl),
    path('del/<int:uid>/', c_v.delp),
    path('edit/<int:uid>/', c_v.edit),
    path('add/', c_v.add),
    path('', c_v.index),
    re_path('^static/(?P<path>.*)$', static.serve, {'document_root': STATIC_ROOT}),
]
