from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .views import RegisterView, UserView

urlpatterns = [
    path('', include('rest_framework.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>', UserView.as_view()),
]
