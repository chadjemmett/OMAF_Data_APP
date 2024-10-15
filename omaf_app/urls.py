from django.urls import path
from . import views

app_name = 'omaf_app'

urlpatterns = [
        path('/', views.index, name='index'),
        path('register', views.register, name='register'),
        path('login', views.login, name='login'),
        path('dashboard', views.dashboard, name='dashboard'),
        ]
