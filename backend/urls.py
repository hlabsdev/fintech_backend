"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken import views as tokenViews
from rest_framework.routers import DefaultRouter
from .api import views

# Un router qui va patcher mes viewsets.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.ProfileViewSet)
router.register(r'zone', views.ZoneSet)
router.register(r'client', views.ClientSet)
router.register(r'compte/epargne', views.EpargneSet)
router.register(r'compte/tontine', views.TontineSet)
router.register(r'moisCotisation', views.MoisCotiseSet)
router.register(r'typecredit/epargne', views.TypeCreditEpargneSet)
router.register(r'typecredit/tontine', views.TypeCreditTontineSet)

# Les Endpoint de l'API

urlpatterns = [
   
    # path('', views.api_root),

    path('admin/', admin.site.urls),
    path('api/auth', include('rest_framework.urls')),
    path('api/get_token/', tokenViews.obtain_auth_token),

    path('api/', include(router.urls)),
    # path('api/admin/', include(admins.admin_urls)),
]
