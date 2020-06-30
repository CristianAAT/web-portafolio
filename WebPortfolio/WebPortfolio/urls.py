from django.contrib import admin
from django.urls import path
from Core.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index')
]
