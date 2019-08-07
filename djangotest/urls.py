from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('articles/', include('articles.url')),
]

urlpatterns += staticfiles_urlpatterns()
