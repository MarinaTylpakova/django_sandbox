from django.urls import include,path
from django.contrib import admin

from polls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
]
