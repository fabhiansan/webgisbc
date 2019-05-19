from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('map/', views.mapviews),
    path('jquery/', views.jquery),
    path('map2/', views.api),
    path('dmsconverter/', views.dmsconverter, name='dmsconverter'),
    path("degreeconverter/", views.degreeconverter, name='degreeconverter'),
    path("fotoudara/", views.fotoudara, name='fotoudara'),
    path('saran/', views.SaranView.as_view(), name='saran'),
    path('403/', views.permission_denied_view),
]