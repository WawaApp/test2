from django.contrib import admin
from django.urls import path, include
from atrip import views
from atrip.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atrip/', include('atrip.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
]