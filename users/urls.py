from django.urls import path
from users.views import home, CreateUser, landingpage
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', landingpage, name='landingpage'),
    path('register/', CreateUser, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html', ), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('home/', home, name='home' ),
]