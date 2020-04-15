from django.urls import path
from user_app import views
from django.contrib.auth import views as auth_views

#Template URL
app_name = 'user_app'

urlpatterns = [
                path('register/', views.register, name = 'register'),
                path('user_login/',views.user_login, name = 'user_login'),
]
