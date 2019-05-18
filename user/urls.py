from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.urls import include, path
from . views import UserCreateView, SaranView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout' ),
    path('saran/', SaranView.as_view(), name='saran')
]