from django.contrib import admin
from django.urls import path
from cameras import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('/add_camera/', views.add_camera, name='add_camera'),
    path('map/', views.map_view, name='map'),
]
