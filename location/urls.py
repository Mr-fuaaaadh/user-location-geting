from django.urls import path,include
from location import views


urlpatterns = [
    path('', views.save_location, name='save_location'),
    path('user_location/<int:id>/', views.view_user_location, name='view_locations'),
    
    
]
