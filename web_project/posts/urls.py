from django.urls import path
from .views import first, main, new
from django.contrib.auth import views as auth_views


app_name = "posts"
urlpatterns = [
    path('first/', first, name="first"),
    path('main/', main, name="main"),
    path('new/', new, name="new"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # django.contrib.auth의 LoginView 그대로 사용
]
