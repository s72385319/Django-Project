from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('incl/', views.incl, name="incl"),
    path('test/', views.test, name="test")
]