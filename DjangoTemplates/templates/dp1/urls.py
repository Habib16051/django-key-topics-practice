
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('app2.urls')),



]
