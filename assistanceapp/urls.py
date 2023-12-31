from django.urls import path
from . import views

urlpatterns = [
    # Login logout urls
    # path('register/', views.login_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # app paths
    path('', views.base, name='base'),
    path('map/', views.map_view, name='map'),
    path('manageLocations/', views.manage_locations, name='manageLocations'),
    path('editLocation/<str:resource_name>/', views.edit_location, name='editLocation'),
    path('deleteLocation/<str:resource_name>/', views.delete_location, name='deleteLocation'),

]
