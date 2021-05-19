"""Bloga URL Configuration

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
from django.urls import path
from posta import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('detail/<int:bloga_id>', views.detail, name="detail"),
    path('create', views.create, name="create"),
    path('update/<int:bloga_id>/', views.update, name='update'),
    path('delete/<int:bloga_id>/', views.delete, name='delete'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT,})
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
